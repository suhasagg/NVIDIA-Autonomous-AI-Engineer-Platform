# Production Runbook

## Start
```bash
cp .env.example .env
docker compose up --build -d
curl http://localhost:8000/health
```

## Exercise
```bash
curl http://localhost:8000/v1/skills -H 'x-api-key: change-me'
curl -X POST http://localhost:8000/v1/goals -H 'x-api-key: change-me' -H 'Content-Type: application/json' --data-binary @examples/goal.json
```

## Diagnose
```bash
docker compose ps
docker compose logs -f api
docker compose exec postgres psql -U postgres -d engineer
```

Production incidents prioritize: stop unsafe dispatch, preserve durable truth, fence stale workers, reconcile ambiguous side effects, restore dependencies, and resume only safe/idempotent work.
