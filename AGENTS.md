# Electrical Apprenticeship Course — Agent Instructions

## Project Overview
Content repository for electrical apprenticeship lessons, exercises, and printable materials. Not a code project — no build, test, or lint toolchain. Tooling is limited to Python helpers in `scripts/course_lib.py` for config validation and markdown parsing.

## Key Files
- `config/course.yaml` — Course metadata, module structure (01–20 × 9 topics), paths, export settings
- `templates/lesson.md` — Lesson authoring template with `{{placeholders}}`
- `templates/exercises.md` — Exercise authoring template
- `scripts/course_lib.py` — Stdlib-only helpers: `load_config()`, `populated_modules()`, markdown parsing

## Module Structure
```
modules/
  NN-TOPIC/          # NN = 01–20, TOPIC ∈ {THEORY,BENDING,RESI,XFRMR,CALC,HZRD,MOTOR,CONTROL,PLC}
    lesson.md        # (template: templates/lesson.md)
    exercises.md     # (template: templates/exercises.md)
    assessment.md    # (template not yet created)
    instructor-notes.md  # (template not yet created)
```
Total: 180 module folders (20 × 9). All exist as empty directories.

## Common Tasks

### Validate config and list expected modules
```bash
python3 -c "from scripts.course_lib import load_config; cfg = load_config(); print('Modules:', len(cfg.module_ids())); print('Topics:', [t.code for t in cfg.topics])"
```

### Check which modules have lesson.md populated
```bash
python3 -c "from scripts.course_lib import load_config, populated_modules; cfg = load_config(); print('Populated:', populated_modules(cfg))"
```

### Load config in a script
```python
from scripts.course_lib import load_config
cfg = load_config()  # reads config/course.yaml
```

## Authoring Conventions
- Replace all `{{placeholders}}` in templates before saving
- Use relative paths for assets: `../../assets/diagrams/filename.png`
- Jurisdiction and code edition must be set in `config/course.yaml` before publishing
- Instructor materials (`instructor-notes.md`, answer keys) excluded from learner exports by default (`include_instructor_notes: false`)

## Paths (from config)
| Purpose | Path |
|---------|------|
| Module root | `modules/` |
| Templates | `templates/` |
| Diagrams | `assets/diagrams/` |
| Images | `assets/images/` |
| Audio | `assets/audio/` |
| Exports (docx) | `exports/docx/` |
| Exports (pdf) | `exports/pdf/` |

## Safety Notes
- Practical exercises must specify PPE, isolation, lockout/tagout, supervision
- Template text explicitly does not authorize energized work
- Qualified instructor review required before use

## Git Notes
- Empty directories not tracked — scaffold preserved via `.gitkeep` files
- Add content files to preserve module folders in git

## Missing / Future Work
- No assessment.md or instructor-notes.md templates yet
- No export toolchain (docx/pdf generation) implemented
- No CI workflows configured
- No license file