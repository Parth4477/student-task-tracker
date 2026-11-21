# Student Task Tracker

A small Flask web app to add, complete and delete study tasks, built to show a full DevOps workflow: Git, Docker, CI/CD and cloud deployment.

**Live app:** https://student-task-tracker-nvbu.onrender.com
**Health check:** https://student-task-tracker-nvbu.onrender.com/health

> The app runs on Render's free tier, so the first load after a quiet period can take about a minute.

## Problem statement

Building, testing and deploying a web app by hand is slow and error-prone. This project automates the whole path, so every push to GitHub is tested, packaged into a Docker image and deployed to the cloud.

## Features

- Add a task
- Mark a task as done
- Delete a task
- `/health` endpoint for monitoring

## Tech stack

| Part | Tool |
|---|---|
| App | Python, Flask |
| Storage | SQLite |
| Tests | pytest |
| Container | Docker |
| CI/CD | GitHub Actions |
| Image registry | Docker Hub (`parth4477/student-task-tracker`) |
| Cloud | Render |

## Architecture

Developer -> GitHub -> GitHub Actions (test, build, push) -> Docker Hub -> Render -> User

## Run locally

```
git clone https://github.com/Parth4477/student-task-tracker.git
cd student-task-tracker
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
py app.py
```

Open http://localhost:5000

## Run the tests

```
pytest
```

## Run with Docker

```
docker build -t student-task-tracker .
docker run -p 5000:5000 student-task-tracker
```

## CI/CD pipeline

The workflow in `.github/workflows/` runs on every push to `main`:

1. Install dependencies and run the tests
2. Build the Docker image
3. Push the image to Docker Hub
4. Render deploys the new image

## Author

Parth, Data Science, DevOps and Cloud Computing 
