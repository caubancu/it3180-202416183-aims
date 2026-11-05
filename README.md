# AIMS-mini — IT3180 Git & GitHub Labs

Repository for the IT3180 Configuration Management practicals (Labs 01–05).

## Requirements
- Python 3.10+
- Standard library only

## Run
```bash
python main.py
python -m unittest discover -s tests -v
```

## Branching model
- `main`: integration branch (the handout calls this `master`; this repository was initialized with GitHub's default branch `main`).
- `feature/*`, `topic/*`, `bugfix/*`, `refactor/*`, `hotfix/*`: short-lived work branches.
- `release/labXX`: frozen submission baselines.

See `docs/submission-report.md` for the evidence-based checklist.