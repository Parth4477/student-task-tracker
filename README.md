# Student Task Tracker

A small Flask web app to add, finish and delete study tasks.
Built to practise a full DevOps workflow: Git, Docker, CI/CD with GitHub Actions, and cloud deployment.

## Run locally
```
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
py app.py
```
Open http://localhost:5000

## Run tests
```
py -m pytest
```

## Endpoints
| Route | Method | What it does |
|---|---|---|
| `/` | GET | Show all tasks |
| `/add` | POST | Add a task |
| `/done/<id>` | POST | Mark a task done |
| `/delete/<id>` | POST | Delete a task |
| `/health` | GET | Health check, returns `{"status":"ok"}` |
