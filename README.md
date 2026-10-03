# NVIDIA Autonomous AI Engineer Platform
## Comprehensive Principal / Staff Engineering Edition

## Executive Architecture

```text
ENGINEERING GOAL
      |
Goal Interpreter
      |
AI Planner / Model Gateway
      |
Typed Task DAG
      |
Compiler + Policy + Skill Registry
      |
Durable SQL State + Transactional Outbox
      |
Kafka / Pulsar
      |
Scheduler
      |
+-----------+--------+-------+------+------------+--------------+
| Research  | Coding | Debug | Test | Simulation | Optimization |
+-----------+--------+-------+------+------------+--------------+
      |
NVIDIA-style Agent Skills
      |
MCP Gateway
      |
cuDF / cuOpt / PhysicsNeMo / CUDA / Profilers / CUDA-Q
      |
OpenShell-Compatible Sandbox Plane
      |
Credential Broker + Network/Filesystem Policy
      |
CPU / GPU Experiment Runtime
      |
Build -> Test -> Simulate -> Benchmark
      |
Evaluator
      |
PASS / REPAIR / REPLAN / HUMAN
      |
Approval
      |
Candidate PR / Existing CI-CD
      |
Audit + Artifacts + OpenTelemetry
```


## Repository Map

```text
app/
  agents.py       specialist agents
  api.py          REST endpoints
  compiler.py     DAG validation
  config.py       environment settings
  db.py           async SQLAlchemy
  domain.py       typed contracts
  evaluator.py    PASS/REPAIR logic
  main.py         FastAPI bootstrap
  mcp.py          MCP integration boundary
  memory.py       six memory layers
  models.py       durable SQL/outbox entities
  planner.py      deterministic planner
  policy.py       risk decision foundation
  runtime.py      dependency-aware execution
  sandbox.py      OpenShell-compatible boundary
  security.py     local auth/action hashing
  service.py      goal-to-runtime coordinator
  skills.py       skill registry
docs/
examples/
tests/
```

## Quick Start — Docker

```bash
unzip nvidia-autonomous-ai-engineer-platform-comprehensive.zip
cd nvidia-autonomous-ai-engineer-platform
cp .env.example .env
docker compose build
docker compose up -d
docker compose ps
curl http://localhost:8000/health
```

List skills:

```bash
curl http://localhost:8000/v1/skills   -H 'x-api-key: change-me'
```

Run the included GPU-regression engineering goal:

```bash
curl -X POST http://localhost:8000/v1/goals   -H 'x-api-key: change-me'   -H 'Content-Type: application/json'   --data-binary @examples/goal.json
```

Open interactive API documentation:

```text
http://localhost:8000/docs
```

## Host Development

```bash
docker compose up -d postgres redis

python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

When the API runs on the host instead of inside Docker, change the PostgreSQL and Redis hostnames in `.env` from `postgres`/`redis` to `localhost`.

```bash
uvicorn app.main:app --reload
pytest -q
ruff check .
```

## Database Inspection

```bash
docker compose exec postgres psql -U postgres -d engineer
```

```sql
\dt
SELECT * FROM runs;
SELECT * FROM steps;
SELECT * FROM approvals;
SELECT * FROM idempotency;
SELECT * FROM outbox;
SELECT * FROM audit;
```

## Logs and Shutdown

```bash
docker compose logs -f api
docker compose logs -f postgres
docker compose logs -f redis

docker compose down
# remove local volumes only when intentionally resetting state
docker compose down -v
```


## 1. Executive Summary

This repository is an independent, production-oriented reference architecture for a secure autonomous engineering platform. It converts an engineering goal into a typed, auditable workflow executed by Research, Debug, Coding, Test, Simulation and Optimization agents. The platform separates probabilistic reasoning from deterministic authorization, durable workflow truth and isolated execution.

## 2. Architecture Principles

The design follows five rules: models propose rather than authorize; plans are typed; SQL owns durable truth; generated code executes only in isolated sandboxes; consequential repository or deployment actions require explicit policy and, where configured, human approval.

## 3. End-to-End Lifecycle

A request passes through identity, goal normalization, planning, DAG compilation, policy checks, scheduling, specialist agents, skills/MCP, isolated CPU/GPU experiments, evaluation, approval, action execution, audit and optional replanning.

## 4. Goal Interpreter

Normalize repository, branch, target hardware, problem statement, success criteria, deadlines, data classification, permitted tools, budget and risk. Ambiguous mandatory inputs should transition the workflow to WAITING_INPUT rather than be invented.

## 5. Planner Contract

A planner emits schema-constrained StepSpec objects. It never directly executes shell commands or arbitrary tool calls. A production LLM planner should be behind a model gateway and its JSON output must validate before entering control flow.

## 6. DAG Compiler

Validate unique keys, dependency existence, acyclicity, capability existence, schemas, permissions, hardware constraints, regional constraints, deadlines and budgets. The current compiler implements graph correctness and is the extension point for richer static analysis.

## 7. Plan Versioning

Replanning creates immutable plan versions. Completed valid artifacts can be reused, but historical plans are never silently edited. Persist planner, prompt, skill, model and policy versions for replay and audit.

## 8. Durable Runtime

Persist run, plan, step, attempt, lease, external operation, approval and artifact references. The production runtime dispatches from a transactional outbox to Kafka/Pulsar and workers claim tasks using leases and fencing tokens.

## 9. Research Agent

Search authorized repositories, documentation, telemetry, profiles, issues and prior experiments. Return evidence references and provenance rather than unsupported conclusions.

## 10. Debug Agent

Build ranked root-cause hypotheses from evidence. Distinguish observed facts, hypotheses and recommended experiments. Diagnosis should be falsifiable.

## 11. Coding Agent

Generate candidate patches, not trusted code. Every patch carries source commit, changed files, rationale, evidence and validation requirements.

## 12. Test Agent

Run unit, integration, regression, fuzz or property tests in an isolated runtime. Return machine-readable results and logs as immutable artifacts.

## 13. Simulation Agent

Own domain simulation boundaries such as PhysicsNeMo-style or CUDA-Q-style experiments. Record environment, inputs, hardware and result artifacts for reproducibility.

## 14. Optimization Agent

Own profiling and accelerated-computing experiments such as CUDA profiling, cuDF-style data processing or cuOpt-style optimization. Compare a candidate against an explicit baseline.

## 15. Supervisor Agent

Coordinate goal decomposition, progress, failures, replanning and final synthesis. The supervisor cannot bypass policy or sandbox requirements.

## 16. Skills Registry

Each skill should have a stable ID, version, owner, description, input/output JSON schemas, risk, required permissions, runtime image, hardware needs, region, cost class, health and deprecation state.

## 17. MCP Gateway

MCP provides governed tool access. A production gateway authenticates workloads, binds trusted tenant identity, filters tool discovery, validates schemas, enforces policy, rate limits, redacts data, applies idempotency and emits audit/telemetry.

## 18. MCP Discovery

Cache discovery by server identity/version and policy context. Discovery does not automatically authorize use. Only admitted tools appear in the capability registry.

## 19. MCP Execution Envelope

Internally normalize tenant, principal, run, step, tool, arguments, deadline, idempotency key and trace context. Identity fields must be injected by trusted runtime infrastructure rather than generated by a model.

## 20. OpenShell-Compatible Sandbox Plane

Treat every agent and generated program as untrusted. The sandbox boundary should enforce filesystem, process, network and resource policy outside the agent process and broker access to approved services.

## 21. Sandbox Lifecycle

CREATE -> PREPARE -> RUN -> COLLECT -> DESTROY. Timeouts and cleanup are mandatory. Persist sandbox image, policy version and execution metadata.

## 22. Credential Broker

Agents should never receive long-lived infrastructure secrets. Use short-lived scoped credentials, opaque handles or a proxy that performs approved calls on behalf of the sandbox.

## 23. Network Isolation

Default-deny egress. Permit only explicitly approved destinations and revalidate DNS/redirects. Block metadata endpoints and private ranges unless explicitly required.

## 24. Filesystem Isolation

Mount only the required repository snapshot and artifact paths. Prefer read-only source plus a disposable writable worktree.

## 25. Resource Isolation

Set CPU, memory, GPU, disk, process-count, network and wall-clock limits. Terminate workloads exceeding policy.

## 26. GPU Scheduler

Model GPU architecture, count, memory, MIG profile, CUDA/driver compatibility, locality and maximum runtime as scheduler constraints. Separate CPU, general GPU, profiling and simulation queues.

## 27. Experiment Reproducibility

Every experiment should record commit, container/image digest, GPU, driver, CUDA/toolchain, dataset, seed, configuration, baseline, candidate and measured metrics.

## 28. CUDA Profiling Workflow

Baseline -> reproduce -> profile -> identify hotspot -> candidate optimization -> correctness test -> benchmark -> evidence package.

## 29. cuDF Application

Use a typed acceleration skill to identify dataframe workloads, run a GPU candidate, validate output equivalence and compare latency/throughput against the baseline.

## 30. cuOpt Application

Represent objective, constraints and solver configuration explicitly. Validate feasibility and compare the optimized result against an accepted baseline.

## 31. PhysicsNeMo Application

Prepare simulation inputs, run in an isolated GPU environment, capture simulation metadata and validate domain metrics before accepting a result.

## 32. CUDA-Q Application

Prepare circuit/experiment configuration, execute through a controlled adapter, preserve backend metadata and validate the returned result.

## 33. Evaluator

Combine deterministic tests, static/security analysis, benchmark thresholds, policy findings and optional model-based critique. Return PASS, REPAIR, REPLAN or HUMAN.

## 34. Repair Loop

A failed evaluation can generate a targeted repair step. Bound maximum repair count, replans, elapsed time, model calls and cost to prevent infinite autonomous loops.

## 35. Human Approval

Consequential actions such as PR creation, merge, deployment or expensive experiments can pause for approval. Approval binds to a canonical hash of exact action semantics.

## 36. Approval Hashing

If branch, patch, target, budget, environment or deployment parameters change, the action hash changes and prior approval becomes invalid.

## 37. Pull Request Agent

A candidate PR should include objective, diagnosis, evidence, diff summary, tests, benchmark results, security findings, risks and rollback notes.

## 38. Deployment Boundary

PR creation and deployment are separate capabilities. Production deployment should remain integrated with the organization's existing CI/CD, policy and progressive-delivery controls.

## 39. Transactional Outbox

Atomically persist workflow state and an outbox event in one database transaction. Publish asynchronously. This prevents the database and event bus from diverging after crashes.

## 40. Event Streaming

Use Kafka/Pulsar for step dispatch, callbacks, evaluation events and audit export. Consumers must be idempotent. Use run ID as a default partition key when per-run ordering matters.

## 41. Worker Leases

Workers claim tasks for a bounded period. Expired work can be reclaimed. A lease alone is insufficient without fencing.

## 42. Fencing Tokens

Increment a monotonic token each time ownership changes. Reject commits from stale workers holding older tokens.

## 43. Idempotency

Use tenant + run + step + action-version scoped keys. Persist request hash and result. Reusing the same key with different semantics is a conflict.

## 44. UNKNOWN Outcomes

If a timeout occurs after a potentially committed external write, mark UNKNOWN. A reconciliation worker checks provider state before deciding success or safe retry.

## 45. Retries

Retry only transient and safe failures. Use exponential backoff, jitter, Retry-After, maximum attempts and a global retry budget.

## 46. Circuit Breakers

Prevent thousands of agents from amplifying a failing service. Use CLOSED -> OPEN -> HALF_OPEN -> CLOSED state.

## 47. Bulkheads

Separate interactive reads, code execution, GPU experiments, simulations and reconciliation into independent pools.

## 48. Backpressure

Bound active workflows, fan-out, queue age, model calls, tool calls, GPU jobs and artifact bytes. Preserve already accepted durable work under overload.

## 49. Cancellation

Cancellation is durable. Propagate to queued tasks, running sandboxes and remote jobs where supported. Already committed external actions may require compensation.

## 50. Compensation

Compensation is a domain action, not database rollback. For example, cancel an experiment reservation or revert a temporary environment.

## 51. Working Memory

Current plan, recent outputs and temporary calculations. It should be reconstructible where possible.

## 52. Session Memory

Bounded continuity for an engineering interaction or project session.

## 53. Episodic Memory

Previous investigations, failures and accepted fixes with evidence and timestamps.

## 54. Semantic Memory

Authorized retrieval over code, documentation, runbooks and technical knowledge.

## 55. Entity Memory

Structured repository, commit, issue, service, experiment, GPU and dependency objects.

## 56. Procedural Memory

Governed engineering preferences such as required benchmark suites. It cannot override policy.

## 57. Memory Write Gate

Classify candidate memory, determine scope, verify provenance, deduplicate/conflict-check and apply retention before persisting.

## 58. Code RAG

Apply repository and tenant authorization before retrieval. Preserve commit/path provenance and avoid treating retrieved instructions as system authority.

## 59. Artifact Service

Profiles, logs, patches, reports and binaries should live in object storage with immutable IDs, hashes, classification, lineage and authorization.

## 60. Enterprise Identity

Represent human principal, tenant, workload, agent, sandbox and tool identities independently.

## 61. OIDC and Workload Identity

Production APIs validate issuer, audience, signature and expiry. Internal services use workload identity/mTLS instead of shared static API keys.

## 62. RBAC and ABAC

RBAC grants coarse roles; ABAC considers repository, branch, environment, risk, data classification, region and hardware.

## 63. Policy Decision Point

Return deterministic ALLOW, DENY, REQUIRE_APPROVAL or REQUIRE_SANDBOX. Models may summarize policy but never grant authority.

## 64. Secret Management

Use KMS/Vault/cloud secret stores. Never put secrets in prompts, memory, logs, traces or artifacts.

## 65. Prompt Injection

README files, issues, web pages, tool output and source comments are untrusted data and cannot grant permissions.

## 66. Tool Injection

A tool is trusted only after administrative admission, schema validation, versioning and policy registration.

## 67. SSRF Defense

Use destination allowlists, DNS/IP validation, redirect revalidation and metadata/private-range blocking.

## 68. Software Supply Chain

Pin and verify dependencies, containers and skills. Produce SBOMs, sign images/artifacts and scan dependencies and source.

## 69. Model Gateway

Centralize model routing, allowlists, privacy policy, token budgets, rate limits, prompt registry, fallback and telemetry.

## 70. Structured Model Output

Planner and evaluator outputs must pass schema validation before becoming executable control flow.

## 71. Observability

Trace goal -> planner -> agent -> skill -> MCP/sandbox -> evaluator -> approval. Use OpenTelemetry, structured logs and Prometheus-compatible metrics.

## 72. Metrics

Track queue lag, oldest task, step latency, GPU utilization, test pass rate, benchmark delta, repair/replan rate, UNKNOWN count, approval wait, model cost and human acceptance.

## 73. Audit

Record actor, tenant, repository, commit, capability, policy decision, sandbox, action hash, artifacts, timestamps and result.

## 74. Multi-Tenancy

Scope SQL, cache, queue, vector retrieval, artifacts, credentials, logs, traces and accelerator quotas by trusted tenant identity.

## 75. Privacy and Data Residency

Minimize proprietary code sent to external models and route data only to approved regions/models.

## 76. Threat Model

Cover malicious repository content, secret exfiltration, dependency attacks, SSRF, sandbox escape, forged callbacks, excessive agency, approval substitution and memory poisoning.

## 77. SQL Source of Truth

Postgres/distributed SQL stores authoritative workflow state. Redis can accelerate cache/rate limits but should not be the only durable state.

## 78. Database Schema

Recommended tables include runs, plan_versions, steps, step_attempts, approvals, idempotency_keys, outbox_events, skills, sandboxes, experiments, artifacts, memory_records and audit_events.

## 79. Transaction Boundaries

Commit state before network work. Never hold a SQL transaction open while calling a model, MCP server, Git provider or GPU job.

## 80. Alembic Migrations

The local project uses create_all for convenience. Production uses explicit expand/contract migrations and backward-compatible rollouts.

## 81. Kubernetes Topology

Separate API/planner/scheduler/evaluator/reconciliation and worker deployments. Use workload identity, NetworkPolicy, HPA, PDB and topology spread.

## 82. GPU Worker Pools

Separate pools by hardware/toolchain and workload type to avoid head-of-line blocking and incompatible environments.

## 83. Autoscaling

Scale on queue lag, oldest task age, pending GPU resource requirements and utilization, not CPU alone.

## 84. Multi-Region

Assign one authoritative execution region per step/run and enforce residency/locality. Prevent duplicate ownership during failover.

## 85. Disaster Recovery

Fence old workers, restore authoritative state, replay unpublished outbox records, reconcile external effects and resume only safe work.

## 86. Capacity Planning

Estimate goals/day x steps/goal, then independently model planner/model throughput, CPU/GPU seconds, SQL writes, queue throughput and artifact bandwidth.

## 87. Cost Governance

Track model tokens, CPU/GPU seconds, API/tool calls and artifact storage per tenant/run. Enforce workflow and tenant budgets.

## 88. CI/CD

Lint, unit/property/contract tests, SAST, dependency/SBOM/image scans, staging workflows, load/chaos/security tests, signing and progressive delivery.

## 89. Property Tests

Assert dependency ordering, approval safety, tenant isolation, idempotency and fencing invariants.

## 90. Contract Tests

For MCP/OpenShell/tool adapters validate authentication, schemas, timeout/error semantics, cancellation and version compatibility.

## 91. Load Testing

Exercise many short tasks, huge DAGs, GPU backlogs, provider slowness and repair storms.

## 92. Chaos Testing

Kill workers, duplicate events, fail the DB leader, restart gateways, timeout tools and lose Redis; verify correctness rather than just uptime.

## 93. Sandbox Security Testing

Test filesystem escape, network bypass, secret access, process limits, resource exhaustion and malicious generated code.

## 94. SLOs

Define control-plane availability, durable acceptance, scheduler start latency and workflow completion separately.

## 95. Incident: Stuck Workflow

Inspect run/plan, oldest nonterminal step, lease/fencing, sandbox/provider state and approvals. Reconcile UNKNOWN before requeueing.

## 96. Incident: GPU Queue Saturation

Apply priority/fairness, enforce budgets, protect interactive work, scale compatible pools and reject or defer low-priority new experiments.

## 97. Incident: Compromised Skill

Disable registry version, revoke credentials, stop dispatch, preserve audit, identify affected runs/artifacts and security-review before re-enable.

## 98. Application: GPU Regression Solver

Telemetry regression -> research suspect changes -> reproduce -> profile -> diagnose -> patch -> test -> benchmark -> approval -> candidate PR.

## 99. Application: CUDA Optimization

Baseline -> profiler -> hotspot -> candidate optimization -> correctness -> benchmark -> evidence.

## 100. Application: Autonomous Debugging

Failure -> logs/traces/code retrieval -> hypothesis -> experiment -> root cause -> candidate patch -> validation.

## 101. Application: Simulation Engineer

Engineering objective -> simulation plan -> GPU sandbox -> simulation -> validation -> report/artifact.

## 102. Application: Code Modernization

Analyze repository -> identify migration candidates -> staged patches -> tests/benchmarks -> human-reviewed PRs.

## 103. Application: CI Failure Repair

Failed CI -> collect evidence -> classify -> reproduce in sandbox -> candidate repair -> rerun tests -> PR suggestion.

## 104. Application: Performance Tuning

Profile service -> rank hotspots -> generate safe candidates -> benchmark -> compare cost/performance -> approval.

## 105. Application: Engineering Research

Question -> source/code research -> evidence graph -> synthesis -> experiments where necessary -> cited technical report.

## 106. Business Value

Measure time-to-diagnosis, engineering hours saved, benchmark improvement, candidate acceptance, false-fix rate, escaped defects, GPU utilization and cost.

## 107. Local Code Walkthrough

domain.py defines contracts; planner.py plans; compiler.py validates; agents.py implements specialists; skills.py registers capabilities; sandbox.py isolates execution; mcp.py connects tools; policy.py gates risk; runtime.py orchestrates; evaluator.py verifies; models.py defines durable foundations; security.py hashes/authenticates; service.py and api.py expose the platform.

## 108. Local vs Production

The local package deliberately runs with deterministic planning and mock tool/sandbox integrations. Real deployment requires NVIDIA SDK/tool installation, GPU fleet integration, organization identity, Git/CI credentials, policy, observability and durability wiring.

## 109. Production Upgrade Sequence

Recommended order: enterprise identity; persisted state transitions; Alembic; outbox; Kafka/Pulsar; scheduler/workers; leases/fencing; idempotency; UNKNOWN/reconciliation; approval-resume; production MCP/OpenShell; GPU scheduler; real SDK adapters; artifacts/memory; OpenTelemetry; Kubernetes; load/chaos/security/DR.

## 110. Principal Framing

The key distinction is between intelligence and authority: the model reasons, the compiler validates, policy authorizes, the durable runtime owns truth, the sandbox contains untrusted execution, evidence verifies results and humans control consequential actions.


## Workflow State Machines

```text
RUN:
CREATED
  -> PLANNING
  -> VALIDATING
  -> READY
  -> RUNNING
       -> WAITING_INPUT
       -> WAITING_APPROVAL
       -> WAITING_EXTERNAL
       -> REPLANNING
       -> CANCEL_REQUESTED
  -> COMPLETED / FAILED / CANCELLED

STEP:
PENDING
  -> READY
  -> RUNNING
       -> WAITING_APPROVAL
       -> WAITING_EXTERNAL
       -> UNKNOWN -> RECONCILING
  -> SUCCEEDED / FAILED / CANCELLED
```

## Transactional Outbox Pattern

```sql
BEGIN;

UPDATE steps
SET status = 'READY'
WHERE id = :step_id;

INSERT INTO outbox_events(event_type, aggregate_id, payload)
VALUES ('STEP_READY', :step_id, :payload);

COMMIT;
```

A publisher retries event delivery independently. Consumers remain idempotent.

## Exactly-Once Reality

Do not promise global exactly-once semantics across Git, CI, GPU schedulers, SaaS tools and external APIs.

```text
at-least-once dispatch
+ scoped idempotency
+ provider operation IDs
+ worker leases/fencing
+ UNKNOWN/reconciliation
+ immutable audit
```

## Six-Layer Engineering Memory

```text
Working Memory
   current plan, outputs, temporary calculations

Session Memory
   bounded interaction/project continuity

Episodic Memory
   previous investigations and outcomes

Semantic Memory
   authorized code/docs/runbook knowledge

Entity Memory
   repos, commits, issues, services, GPUs, experiments

Procedural Memory
   governed engineering preferences and processes
```

**Memory provides context. It never grants authorization.**

## Production Service Decomposition

```text
services/
  api/
  goal/
  planner/
  compiler/
  scheduler/
  runtime-worker/
  research-worker/
  debug-worker/
  coding-worker/
  test-worker/
  simulation-worker/
  optimization-worker/
  skill-registry/
  model-gateway/
  mcp-gateway/
  sandbox-gateway/
  gpu-scheduler/
  evaluator/
  approval/
  reconciliation/
  memory/
  artifact-service/
  audit-exporter/
```

## Recommended Production Tables

```text
runs
plan_versions
steps
step_attempts
worker_leases
approvals
idempotency_keys
outbox_events
workflow_events
skills
mcp_servers
sandboxes
experiments
artifacts
memory_records
audit_events
```

## Suggested Indexes

```text
steps(status, not_before)
steps(run_id, plan_version, step_key)
worker_leases(step_id, expires_at)
outbox_events(published, created_at)
approvals(status, created_at)
artifacts(run_id, created_at)
audit_events(run_id, created_at)
```

## Production Kubernetes Topology

```text
Ingress / API Gateway
          |
   Control Plane APIs
          |
 Planner / Compiler / Policy
          |
 PostgreSQL / Distributed SQL
          |
       Outbox
          |
    Kafka / Pulsar
          |
       Scheduler
          |
 +--------+---------+----------+-----------+
 | CPU    | Coding  | GPU      | Simulation|
 | Worker | Worker  | Workers  | Workers   |
 +--------+---------+----------+-----------+
          |
 MCP Gateway / Sandbox Gateway
          |
 Git / CI / CUDA / NVIDIA SDKs / Engineering Systems
```

## Example GPU Regression Workflow

```text
Performance alert
      |
Research Agent
      |
Code + telemetry evidence
      |
Debug Agent
      |
Root-cause hypotheses
      |
Reproduction Sandbox
      |
CUDA Profiler
      |
Coding Agent
      |
Candidate patch
      |
Test Agent
      |
Benchmark
      |
Evaluator
  /       \
REPAIR    PASS
 |         |
 +------> Approval
             |
        Candidate PR
```

## Example Evaluation Contract

```json
{
  "decision": "PASS",
  "checks": {
    "unit_tests": "PASS",
    "integration_tests": "PASS",
    "correctness": "PASS",
    "benchmark": "PASS",
    "security": "PASS",
    "policy": "PASS"
  },
  "evidence": [
    "artifact://test-report",
    "artifact://profile",
    "artifact://benchmark"
  ]
}
```

## Example Approval Record

```json
{
  "run_id": "...",
  "step_key": "create_pr",
  "action_hash": "...",
  "risk": "HIGH",
  "summary": "Create PR against main with validated candidate patch",
  "required_role": "repository_approver",
  "status": "PENDING"
}
```

## Production Readiness Checklist

```text
[ ] OIDC and workload identity
[ ] trusted tenant derivation
[ ] RBAC/ABAC and policy-as-code
[ ] persistent state transitions
[ ] Alembic migrations
[ ] transactional outbox publisher
[ ] Kafka/Pulsar
[ ] durable scheduler and worker pools
[ ] leases and fencing
[ ] idempotency wired into writes
[ ] UNKNOWN/reconciliation
[ ] cancellation and compensation
[ ] approval decision/resume API
[ ] production MCP gateway
[ ] production OpenShell/sandbox integration
[ ] signed skills/images/SBOM
[ ] GPU scheduler and quotas
[ ] real CUDA/cuDF/cuOpt/PhysicsNeMo/CUDA-Q adapters as required
[ ] artifact object storage
[ ] persistent governed memory
[ ] model gateway
[ ] DLP and egress controls
[ ] OpenTelemetry
[ ] Kubernetes
[ ] load, chaos, security and sandbox testing
[ ] backup and DR drills
```

## Troubleshooting

### API returns 401

Confirm `.env` and the request use the same `x-api-key`.

### Database connection fails

Inside Docker use hostname `postgres`. When running the API on the host, use `localhost`.

### Plan fails compilation

Check duplicate step keys, missing dependencies, invalid enum values and cycles.

### MCP or sandbox endpoint is unavailable

The default `TOOL_MODE=mock` keeps local development independent of external infrastructure. For real mode, configure endpoints, authentication, schemas and contract tests.

### Workflow stops at approval

This is intentional. High-risk actions are not automatically executed. A production version persists approval decisions and resumes the workflow after validating the exact action hash.

### No GPU is present

Local mock mode does not require one. Real CUDA/NVIDIA workloads require compatible hardware, drivers, SDK/toolchain and scheduler integration.

## Code-to-Architecture Mapping

```text
domain.py
  -> typed contracts

planner.py
  -> goal-to-plan

compiler.py
  -> structural correctness

skills.py
  -> bounded capability catalog

agents.py
  -> specialist intelligence

policy.py
  -> deterministic risk decisions

sandbox.py
  -> isolated execution boundary

mcp.py
  -> governed tool integration

runtime.py
  -> orchestration

evaluator.py
  -> evidence-based verification

memory.py
  -> governed context layers

models.py
  -> durable-state/outbox foundation

security.py
  -> local authentication + action binding

service.py / api.py
  -> control-plane surface
```

## Important Production Boundary

This repository is intentionally honest about what a generic downloadable package can and cannot guarantee. It is a substantive runnable reference implementation, but true production deployment depends on the target organization's NVIDIA SDK versions, GPU fleet, drivers, Git/CI providers, identity system, secrets infrastructure, network topology, compliance rules, SLOs and security controls.

The package therefore does **not** fabricate NVIDIA credentials, proprietary APIs, GPU benchmark results or claims of being NVIDIA internal source code.

## Principal-Level Design Summary

```text
Model        -> reasons and proposes
Planner      -> creates typed work
Compiler     -> validates structure/contracts
Policy       -> decides authority
SQL Runtime  -> owns durable execution truth
Skills       -> expose bounded engineering capabilities
MCP          -> provides governed tool access
Sandbox      -> contains untrusted execution
GPU Runtime  -> executes accelerated experiments
Evaluator    -> verifies tests/benchmarks/evidence
Approval     -> controls consequential actions
Audit        -> reconstructs the system
```

**The model proposes. The compiler validates. Policy authorizes. The sandbox contains. The runtime owns truth. Evidence proves the result. Humans retain control over consequential actions.**
