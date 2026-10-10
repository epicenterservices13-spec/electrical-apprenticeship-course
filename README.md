# Electrical Apprenticeship Course

A workspace for developing electrical apprenticeship lessons, practical exercises, diagrams, and printable course materials.

The repository currently contains a directory scaffold. Lessons, templates, configuration, build scripts, and automation have not yet been added.

## Directory structure

```text
electrical-apprenticeship-course/
├── config/                 # Course settings and export configuration
├── templates/              # Reusable lesson, worksheet, and assessment templates
├── modules/                # 180 folders: numbers 01–20 × nine topic codes
│   ├── 01-THEORY/
│   ├── 01-BENDING/
│   ├── ...
│   └── 20-PLC/
├── assets/
│   ├── diagrams/           # Circuit diagrams, schematics, and drawings
│   ├── images/             # Photos and other illustrations
│   └── audio/              # Narration and audio learning materials
├── scripts/                # Future validation and export utilities
├── exports/
│   ├── docx/               # Generated Word documents
│   └── pdf/                # Generated PDF documents
└── .github/
    └── workflows/          # Future GitHub Actions workflows
```

## Module naming

Module folders follow the convention `NN-TOPIC`, where `NN` is a two-digit number from `01` to `20`. Every number has a folder for each topic below; these folders do not yet define a lesson sequence.

| Code | Intended topic |
| --- | --- |
| `THEORY` | Electrical theory |
| `BENDING` | Conduit bending |
| `RESI` | Residential wiring |
| `XFRMR` | Transformers |
| `CALC` | Electrical calculations |
| `HZRD` | Electrical hazards and safety |
| `MOTOR` | Motors |
| `CONTOL` | Controls |
| `PLC` | Programmable logic controllers |

`CONTOL` preserves the spelling used when the folders were created. Use this exact code in paths unless the folders and their references are renamed together.

## Adding course materials

1. Choose the appropriate numbered topic folder under `modules/`.
2. Add a lesson with learning objectives, prerequisites, explanations, worked examples, and references.
3. Add practical exercises and assessments as needed, with instructor guidance and answer keys kept clearly identified.
4. Store shared media under `assets/` and reference it using relative paths.
5. Use `templates/` for formats shared across lessons.

A suggested layout for a populated module is:

```text
modules/01-THEORY/
├── lesson.md
├── exercises.md
├── assessment.md
└── instructor-notes.md
```

When authoring lessons, specify units, assumptions, the applicable jurisdiction, and the edition of any electrical code or standard cited. Record image sources and permissions, and include descriptive text for diagrams.

## Exporting materials

Reserve `exports/docx/` and `exports/pdf/` for generated deliverables. Keep editable source materials in `modules/`, `templates/`, and `assets/`.

No export commands or software dependencies are configured yet. When an export toolchain is added, document its installation requirements and commands here, and place reusable build utilities in `scripts/`.

## Instructional safety

Course materials support supervised instruction. Practical exercises should state required protective equipment, isolation procedures, tools, and instructor supervision. Have a qualified instructor review technical content and safety procedures before use, following applicable local requirements.

## Version control

Git does not track empty directories. Add course files or `.gitkeep` placeholders to preserve the scaffold when committing it.

## License

No license has been selected. Add a `LICENSE` file before distributing materials under defined reuse terms.
