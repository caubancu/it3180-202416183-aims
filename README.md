# AIMS-mini — IT3180

Repository for the IT3180 Git & GitHub practical labs (01–05).

## Requirements
- Python 3.10+
- Standard library only

## Run
```bash
python main.py
python -m unittest discover -s tests -v
```

## Branch model
`main` is the integration branch (equivalent to `master` in the handout). Short-lived `feature/*`, `topic/*`, `bugfix/*`, `refactor/*` and `hotfix/*` branches are merged by Pull Request. `release/labXX` branches are submission snapshots.

See `docs/submission-report.md` for the implementation status and evidence.