# hng14-stage2-devops
# HNG Stage 2 - DevOps Task

This project is a containerized microservices application consisting of a Node.js frontend, a Python API, and a Python Worker, all coordinated by Redis.

## How to Start the App
1.  **Clone the repo:** `git clone https://github.com/BlessingbillCloudify/hng14-stage2-devops.git`
2.  **Set up secrets:** Copy `.env.example` to `.env` and fill in your `REDIS_PASSWORD`.
3.  **Run the Stack:** `docker-compose up --build`
4.  **Verify:** Visit `http://localhost:3000` to submit jobs.

## Architecture
- **Frontend (Port 3000):** Node.js/Express proxy for the UI.
- **API (Port 8000):** FastAPI service for job creation.
- **Worker:** Background processor for jobs.
- **Redis:** Message broker and status store.
