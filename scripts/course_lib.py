"""Shared helpers for course tooling: config loading and markdown parsing.

Standard library only, so the scripts run on Termux and CI without pip.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
LEARNER_FILES = ("lesson", "exercises", "assessment")


class ConfigError(ValueError):
    """Raised when course.yaml cannot be parsed or is missing required keys."""


# --------------------------------------------------------------------------
# Minimal YAML loader (block mappings, block lists, scalars, comments).
# --------------------------------------------------------------------------

def _scalar(raw: str) -> Any:
    raw = raw.strip()
    if raw in ("", "~", "null", "Null", "NULL"):
        return None
    if raw in ("true", "True"):
        return True
    if raw in ("false", "False"):
        return False
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    return raw


def _strip_comment(line: str) -> str:
    quote = None
    for i, ch in enumerate(line):
        if ch in "\"'":
            quote = None if quote == ch else (quote or ch)
        elif ch == "#" and quote is None and (i == 0 or line[i - 1].isspace()):
            return line[:i].rstrip()
    return line.rstrip()


def load_yaml(text: str) -> Any:
    """Parse the YAML subset used by config/course.yaml."""
    lines: list[tuple[int, str, int]] = []
    for lineno, raw in enumerate(text.splitlines(), 1):
        if "\t" in raw[: len(raw) - len(raw.lstrip())]:
            raise ConfigError(f"line {lineno}: tabs are not allowed for indentation")
        stripped = _strip_comment(raw)
        if stripped.strip():
            lines.append((len(stripped) - len(stripped.lstrip()), stripped.strip(), lineno))

    pos = 0

    def parse_block(indent: int) -> Any:
        nonlocal pos
        if pos >= len(lines):
            return None
        is_list = lines[pos][1].startswith("- ") or lines[pos][1] == "-"
        result: Any = [] if is_list else {}
        while pos < len(lines):
            ind, content, lineno = lines[pos]
            if ind < indent:
                break
            if ind > indent:
                raise ConfigError(f"line {lineno}: unexpected indentation")
            if is_list:
                if not (content.startswith("- ") or content == "-"):
                    raise ConfigError(f"line {lineno}: expected list item")
                item = content[1:].strip()
                if not item:
                    pos += 1
                    result.append(parse_block(lines[pos][0]) if pos < len(lines) and lines[pos][0] > ind else None)
                elif re.match(r"^[^\"'][^:]*:(\s|$)", item):
                    # Inline first key of a mapping item: re-read it at a deeper indent.
                    lines[pos] = (ind + 2, item, lineno)
                    result.append(parse_block(ind + 2))
                else:
                    result.append(_scalar(item))
                    pos += 1
            else:
                m = re.match(r"^([^:]+?):(?:\s+(.*))?$", content)
                if not m:
                    raise ConfigError(f"line {lineno}: expected 'key: value'")
                key, value = m.group(1).strip(), m.group(2)
                pos += 1
                if value is None or value == "":
                    if pos < len(lines) and lines[pos][0] > ind:
                        result[key] = parse_block(lines[pos][0])
                    elif pos < len(lines) and lines[pos][0] == ind and lines[pos][1].startswith("-"):
                        result[key] = parse_block(ind)
                    else:
                        result[key] = None
                else:
                    result[key] = _scalar(value)
        return result

    data = parse_block(lines[0][0]) if lines else {}
    if pos != len(lines):
        raise ConfigError(f"line {lines[pos][2]}: could not parse")
    return data


# --------------------------------------------------------------------------
# Config model
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Topic:
    code: str
    title: str


@dataclass(frozen=True)
class Config:
    title: str
    description: str
    jurisdiction: str | None
    code_name: str | None
    code_edition: str | None
    modules_root: str
    number_start: int
    number_end: int
    padding: int
    pattern: str
    topics: tuple[Topic, ...]
    content_files: dict[str, str] = field(default_factory=dict)
    paths: dict[str, str] = field(default_factory=dict)
    exports: dict[str, Any] = field(default_factory=dict)

    @property
    def code_label(self) -> str:
        parts = [p for p in (self.code_name, str(self.code_edition or "")) if p]
        return " ".join(parts)

    def topic(self, code: str) -> Topic:
        for t in self.topics:
            if t.code == code:
                return t
        raise KeyError(code)

    def module_ids(self) -> list[str]:
        """Every expected module folder name, ordered by number then topic."""
        return [
            self.pattern.format(number=str(n).zfill(self.padding), topic=t.code)
            for n in range(self.number_start, self.number_end + 1)
            for t in self.topics
        ]

    def module_dir(self, root: Path, module_id: str) -> Path:
        return root / self.modules_root / module_id


def _require(d: Any, key: str, ctx: str) -> Any:
    if not isinstance(d, dict) or key not in d:
        raise ConfigError(f"missing required key '{ctx}{key}'")
    return d[key]


def load_config(root: Path = REPO_ROOT) -> Config:
    path = root / "config" / "course.yaml"
    try:
        data = load_yaml(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigError(f"{path} not found") from exc
    course = _require(data, "course", "")
    mods = _require(data, "modules", "")
    code = course.get("electrical_code") or {}
    topics = tuple(
        Topic(str(_require(t, "code", "modules.topics[].")), str(_require(t, "title", "modules.topics[].")))
        for t in _require(mods, "topics", "modules.") or []
    )
    if not topics:
        raise ConfigError("modules.topics must not be empty")
    return Config(
        title=str(_require(course, "title", "course.")),
        description=str(course.get("description") or ""),
        jurisdiction=course.get("jurisdiction"),
        code_name=code.get("name"),
        code_edition=None if code.get("edition") is None else str(code.get("edition")),
        modules_root=str(mods.get("root", "modules")),
        number_start=int(_require(mods, "number_start", "modules.")),
        number_end=int(_require(mods, "number_end", "modules.")),
        padding=int(mods.get("number_padding", 2)),
        pattern=str(mods.get("directory_pattern", "{number}-{topic}")),
        topics=topics,
        content_files=dict(_require(mods, "content_files", "modules.")),
        paths=dict(data.get("paths") or {}),
        exports=dict(data.get("exports") or {}),
    )


# --------------------------------------------------------------------------
# Markdown helpers
# --------------------------------------------------------------------------

def h1(md: str) -> str:
    m = re.search(r"^# (.+)$", md, re.M)
    return m.group(1).strip() if m else ""


def module_title(md: str) -> str:
    """'01-THEORY: Voltage... — Exercises' -> 'Voltage...'."""
    title = h1(md)
    title = title.split(":", 1)[1] if ":" in title else title
    return title.split(" — ")[0].strip()


def h2_sections(md: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^## (.+)$", strip_code(md), re.M)]


def section(md: str, heading: str) -> str:
    """Body of the first H2 whose title starts with `heading` (case-insensitive)."""
    lines = md.splitlines()
    out: list[str] = []
    inside = False
    for line in lines:
        if line.startswith("## "):
            if inside:
                break
            inside = line[3:].strip().lower().startswith(heading.lower())
            continue
        if inside:
            out.append(line)
    return "\n".join(out).strip()


def strip_code(md: str) -> str:
    return re.sub(r"```.*?```", "", md, flags=re.S)


def parse_tables(md: str) -> list[list[dict[str, str]]]:
    """All pipe tables in `md`, each as a list of row dicts keyed by header."""
    tables: list[list[dict[str, str]]] = []
    block: list[str] = []
    for line in strip_code(md).splitlines() + [""]:
        if line.strip().startswith("|"):
            block.append(line.strip())
            continue
        if len(block) >= 2 and re.fullmatch(r"\|[\s:\-|]+\|", block[1]):
            split = lambda r: [c.strip() for c in r.strip("|").split("|")]
            headers = split(block[0])
            tables.append([dict(zip(headers, split(r))) for r in block[2:]])
        block = []
    return tables


def header_fields(md: str) -> dict[str, str]:
    """The Field | Value metadata table at the top of a content file."""
    for table in parse_tables(md):
        if table and "Field" in table[0] and "Value" in table[0]:
            return {r["Field"]: r["Value"] for r in table}
    return {}


def clean_inline(text: str) -> str:
    """Remove markdown emphasis/backticks and bold markers from a table cell."""
    return re.sub(r"[*`]", "", text).strip()


def populated_modules(cfg: Config, root: Path = REPO_ROOT) -> list[str]:
    lesson = cfg.content_files.get("lesson", "lesson.md")
    return [m for m in cfg.module_ids() if (cfg.module_dir(root, m) / lesson).is_file()]
