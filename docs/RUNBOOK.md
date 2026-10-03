# Runbook

```bash
cp .env.example .env
docker compose up --build -d
curl http://localhost:8000/health
curl -X POST http://localhost:8000/v1/goals -H 'x-api-key: change-me' -H 'Content-Type: application/json' --data-binary @examples/goal.json
docker compose logs -f api
pytest -q
```
