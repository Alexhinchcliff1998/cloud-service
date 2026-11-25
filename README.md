# OpsStatus | Containerized Operations API

FastAPI service for fictional dependency health checks, with Docker packaging and an AWS ECS Fargate deployment blueprint.

```bash
pip install -r requirements.txt
uvicorn service:app --host 127.0.0.1 --port 8080
python -m pytest -q
# docker build -t opsstatus .
# docker run --rm -p 127.0.0.1:8080:8080 opsstatus
```
Explore /docs, /health, /ready and POST /v1/summary. Availability describes supplied check observations, not measured uptime. See infra/DEPLOYMENT.md. No live AWS deployment or Docker build is claimed. Independent AI-assisted demonstration, not production software.
