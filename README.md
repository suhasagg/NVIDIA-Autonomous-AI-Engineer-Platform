# NVIDIA Autonomous AI Engineer Platform
## Secure Durable GPU-Aware Agentic Engineering Runtime


```text
ENGINEERING GOAL
 -> Goal Interpreter
 -> Planner
 -> Typed Task DAG
 -> Durable Runtime
 -> Research / Coding / Debug / Test / Simulation / Optimization Agents
 -> Skills Registry
 -> MCP Gateway
 -> cuDF / cuOpt / PhysicsNeMo / CUDA / Profilers / CUDA-Q boundaries
 -> OpenShell-compatible isolated sandbox plane
 -> CPU/GPU Experiment Runtime
 -> Build / Test / Simulate / Benchmark
 -> Evaluator
 -> PASS / REPAIR / REPLAN
 -> Human Approval
 -> Candidate PR / Deployment
```

## Quick start
```bash
unzip nvidia-autonomous-ai-engineer-platform.zip
cd nvidia-autonomous-ai-engineer-platform
cp .env.example .env
docker compose build
docker compose up -d
curl http://localhost:8000/health
curl http://localhost:8000/v1/skills -H 'x-api-key: change-me'
curl -X POST http://localhost:8000/v1/goals -H 'x-api-key: change-me' -H 'Content-Type: application/json' --data-binary @examples/goal.json
```

## Host development
```bash
docker compose up -d postgres redis
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
# change postgres/redis hostnames in .env to localhost
uvicorn app.main:app --reload
pytest -q
ruff check .
```

## Production topology
```text
API -> Planner/Model Gateway -> Compiler/Policy/Skills
 -> Distributed SQL + Transactional Outbox -> Kafka/Pulsar
 -> Scheduler -> CPU/GPU Worker Pools
 -> MCP + OpenShell/Sandbox Gateways
 -> Engineering/CUDA/Git/CI systems
 -> Artifacts/Evaluator/Reconciliation
 -> Approval -> PR/CI-CD
 -> Audit/OpenTelemetry
```

## 1. Goal Interpretation

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 2. Typed Ai Planning

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 3. Dag Compilation

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 4. Durable Workflow State

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 5. Research Agent

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 6. Coding Agent

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 7. Debug Agent

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 8. Test Agent

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 9. Simulation Agent

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 10. Optimization Agent

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 11. Nvidia-Style Skills Registry

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 12. Mcp Gateway

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 13. Openshell-Compatible Sandbox Plane

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 14. Credential Brokerage

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 15. Deny-By-Default Network Policy

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 16. Ephemeral Filesystem Isolation

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 17. Cpu/Gpu Experiment Runtime

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 18. Gpu Resource Scheduling

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 19. Cuda Profiling Boundary

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 20. Cudf Acceleration Workflow

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 21. Cuopt Optimization Workflow

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 22. Physicsnemo Simulation Boundary

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 23. Cuda-Q Experiment Boundary

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 24. Reproducible Benchmarks

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 25. Evidence And Artifact Lineage

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 26. Evaluation And Repair Loops

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 27. Human Approval

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 28. Canonical Action Hashing

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 29. Candidate Pr Generation

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 30. Deployment Separation

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 31. Plan Versioning

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 32. Transactional Outbox

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 33. Kafka/Pulsar Event Streaming

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 34. Worker Leases

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 35. Fencing Tokens

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 36. Idempotency

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 37. Unknown And Reconciliation

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 38. Retry Budgets

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 39. Circuit Breakers

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 40. Bulkheads

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 41. Backpressure

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 42. Cancellation

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 43. Saga Compensation

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 44. Six-Layer Memory

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 45. Memory Governance

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 46. Code Rag

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 47. Knowledge Retrieval Authorization

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 48. Enterprise Identity

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 49. Workload Identity

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 50. Rbac

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 51. Abac

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 52. Deterministic Policy

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 53. Secret Management

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 54. Dlp

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 55. Prompt Injection

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 56. Indirect Prompt Injection

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 57. Tool Injection

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 58. Ssrf Defense

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 59. Software Supply-Chain Security

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 60. Sbom And Signing

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 61. Model Gateway

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 62. Model Routing

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 63. Structured Model Output

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 64. Opentelemetry

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 65. Metrics

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 66. Audit

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 67. Multi-Tenancy

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 68. Privacy

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 69. Data Residency

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 70. Sql Source Of Truth

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 71. Redis Role

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 72. Object Storage

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 73. Database Indexing

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 74. Transaction Boundaries

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 75. Alembic Migrations

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 76. Kubernetes Topology

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 77. Gpu Worker Pools

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 78. Autoscaling

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 79. Multi-Region Execution

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 80. Disaster Recovery

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 81. Rpo/Rto

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 82. Capacity Planning

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 83. Cost Accounting

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 84. Gpu/Model Budgets

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 85. Ci/Cd

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 86. Property Tests

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 87. Contract Tests

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 88. Load Tests

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 89. Chaos Tests

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 90. Sandbox Escape Testing

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 91. Slos

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 92. Incident Response

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 93. Gpu Regression Workflow

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 94. Performance Optimization Workflow

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 95. Simulation Workflow

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 96. Code Review Workflow

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 97. Human Handoff

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 98. Business Value Measurement

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 99. Production Upgrade Path

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## 100. Principal Framing

A production implementation treats this as a governed, versioned capability with explicit contracts, identity, policy, observability, failure semantics and testability. The local repository provides the executable boundary or foundation; enterprise deployment wires it to durable workers, organization credentials, real GPU/tooling infrastructure and environment-specific controls.

## Workflow states
```text
CREATED -> PLANNING -> VALIDATING -> READY -> RUNNING
  -> WAITING_INPUT / WAITING_APPROVAL / REPLANNING
  -> COMPLETED / FAILED / CANCELLED

PENDING -> READY -> RUNNING
  -> SUCCEEDED / FAILED / UNKNOWN -> RECONCILING
  -> WAITING_APPROVAL / CANCELLED
```

## Exactly-once reality
Across Git, CI, GPU schedulers and external tools use:
```text
at-least-once dispatch + idempotency + provider IDs
+ leases/fencing + UNKNOWN/reconciliation + immutable audit
```

## Multi-layer memory
```text
Working    current execution context
Session    interaction continuity
Episodic   previous engineering outcomes
Semantic   code/docs knowledge
Entity     repos/commits/issues/experiments
Procedural governed engineering preferences
```
Memory never grants authorization.

## Production upgrade checklist
```text
OIDC/workload identity
persistent state transitions
Alembic
outbox publisher
Kafka/Pulsar
durable scheduler/workers
leases/fencing
idempotency
UNKNOWN/reconciliation
approval resume API
production MCP gateway
production OpenShell integration
signed skills/images/SBOM
GPU scheduler
real CUDA/cuDF/cuOpt/PhysicsNeMo/CUDA-Q adapters where needed
artifact object storage
persistent governed memory
model gateway
OpenTelemetry
Kubernetes
load/chaos/security/DR validation
```

## Important boundary
This project does not fabricate NVIDIA APIs, credentials or benchmark results. Real production integration depends on installed NVIDIA SDKs, GPU fleet, driver/toolchain versions, organization identity, Git/CI systems, network/security policy, SLOs and compliance requirements.

## Principal-level rule
```text
Model -> proposes
Planner -> creates typed work
Compiler -> validates
Policy -> authorizes
Runtime -> owns durable truth
Skills/MCP -> expose governed capabilities
OpenShell/Sandbox -> contains execution
GPU runtime -> executes experiments
Evaluator -> verifies evidence
Approval -> controls consequential actions
Audit -> reconstructs everything
```

# Comprehensive Production Architecture Guide

## 1. Public NVIDIA alignment

NemoClaw, OpenShell, managed MCP, agent lifecycle, managed inference and secure sandbox execution provide the public architectural grounding. Keep NVIDIA-specific adapters versioned because these products evolve quickly.

## 2. NemoClaw architecture mapping

Map the host/operator lifecycle to the control plane, OpenShell gateway to sandbox/credential/network policy, managed MCP to the tool plane, and agent runtimes to specialist engineering workers.

## 3. OpenShell security boundary

Policy enforcement lives outside the agent process. The agent is assumed capable of making unsafe requests; the runtime constrains filesystem, process, network, credentials and inference routes.

## 4. Agent lifecycle management

Provision, readiness-check, start, pause, snapshot, restore, rebuild, upgrade and destroy are explicit lifecycle operations rather than incidental container commands.

## 5. Versioned blueprints

Pin agent runtime, integration layer, policy schema, image digest and tool versions. Upgrade through compatibility checks and staged rollout.

## 6. Managed inference

Route inference through an approved gateway so model credentials and data-routing policy remain outside the sandbox.

## 7. Managed MCP

Register authenticated MCP servers administratively, enforce request policy, inject credentials at approved boundaries and expose only required tools.

## 8. Progressive tool disclosure

Do not inject the full enterprise tool catalog into every prompt. Discover and reveal capabilities based on task, identity and policy.

## 9. Engineering goal contract

Capture repository, commit/branch, hardware target, workload, constraints, success metrics, maximum cost, maximum time and allowed side effects.

## 10. Success criteria

Require measurable criteria such as tests pass, no security regression, p95 latency improvement, memory bound and benchmark confidence interval.

## 11. Planner contract

Planner emits a typed DAG and rationale/evidence references, not executable shell text. Runtime maps capability IDs to trusted implementations.

## 12. Static plan validation

Validate graph, schemas, capability versions, permissions, GPU requirements, budgets, deadlines, policy and incompatible concurrent mutations.

## 13. Dynamic plan validation

Before dispatch, re-check current authorization, repository state, connector health, available GPU capacity and stale evidence.

## 14. Research agent design

Search source, docs, traces, profiles, issue history and prior experiments. Return evidence objects with source, commit/version and confidence.

## 15. Debug agent design

Generate ranked hypotheses and specify discriminating experiments instead of jumping directly to a patch.

## 16. Coding agent design

Create a candidate diff in an isolated worktree. Never give generated code merge/deploy authority.

## 17. Test agent design

Execute deterministic suites in a clean sandbox; preserve command, image, environment and output artifact.

## 18. Simulation agent design

Translate domain inputs into versioned PhysicsNeMo/CUDA-Q-style experiment specifications and collect reproducible artifacts.

## 19. Optimization agent design

Compare baseline/candidate under controlled hardware and workload conditions and reject statistically weak improvements.

## 20. Code-review agent

Review the candidate independently from the authoring agent where practical; inspect correctness, security, maintainability and evidence.

## 21. Skill manifest

A skill needs ID/version, owner, input/output schema, risk, runtime, hardware, permissions, timeout, artifact contract and evaluation criteria.

## 22. Skill admission

New skills require code review, security review, tests, signed artifact/image and registry approval.

## 23. Skill versioning

In-flight runs keep their pinned skill version. Never replace behavior under an executing workflow.

## 24. MCP server registry

Store server identity, transport, trust tier, supported protocol/version, tool metadata, credential source and health.

## 25. MCP request enforcement

Validate method/tool, JSON schema, tenant/repo scope, arguments, network destination, rate limit, approval and audit before forwarding.

## 26. MCP credential custody

Store bearer/API credentials outside the agent sandbox and replace opaque placeholders only at the trusted proxy boundary.

## 27. Sandbox admission

Validate image digest, agent/runtime version, policy compatibility, GPU needs and host readiness before creation.

## 28. Sandbox filesystem

Use immutable base image plus explicit writable workspace. Protect host paths, Docker socket, credentials and kernel interfaces.

## 29. Sandbox networking

Deny by default. Allow approved package indexes, inference endpoints, MCP servers and organization services with destination validation.

## 30. Sandbox process controls

Limit process tree, capabilities, syscalls where supported, wall time, CPU/RAM/GPU, file descriptors and child process count.

## 31. GPU injection

GPU access is an explicit scheduler/admission decision, not a default property of every agent.

## 32. Credential broker

The agent asks for an operation; the broker authenticates to the destination without returning the raw secret.

## 33. Artifact store

Profiles, logs, traces, diffs, test reports, binaries and simulation outputs receive immutable content hashes and lineage.

## 34. Evidence graph

Link goal -> hypothesis -> experiment -> artifact -> metric -> decision -> patch so the final PR is auditable.

## 35. Experiment specification

Record repository SHA, container digest, GPU, driver, CUDA/tool versions, dataset/workload, seed, warmup, repetitions and metric definitions.

## 36. Benchmark methodology

Use warmup, repeated samples, variance/confidence reporting and equivalent baseline/candidate conditions.

## 37. Performance regression detection

Separate noisy telemetry from statistically meaningful regression before invoking expensive autonomous investigation.

## 38. Profiler workflow

Capture profiler evidence, identify hotspots, formulate hypothesis, create candidate, rerun profiler and compare.

## 39. CUDA workflow

Pin architecture/toolchain and validate correctness before accepting speedup. Treat kernel compilation/runtime errors as evidence, not prompts to bypass policy.

## 40. cuDF workflow

Validate semantic equivalence and data types before comparing accelerated dataframe performance.

## 41. cuOpt workflow

Persist optimization formulation, constraints, solver configuration and objective values so results are reproducible.

## 42. PhysicsNeMo workflow

Version physical model, boundary/initial conditions, mesh/data, precision and validation metrics.

## 43. CUDA-Q workflow

Version circuit/kernel, backend, shots/configuration and result statistics; isolate expensive or remote execution behind policy.

## 44. CPU fallback

When GPU is unavailable, planner can select an approved CPU diagnostic path if it still satisfies the goal.

## 45. GPU scheduler

Schedule by GPU family, memory, count, MIG profile, locality, driver/toolchain compatibility, quota and priority.

## 46. GPU quotas

Apply tenant/team/project quotas and prevent a planner from escalating resource requests.

## 47. GPU preemption

Only preempt workloads with compatible checkpoint/restart semantics; otherwise queue.

## 48. Distributed scheduler

SQL owns state; queue carries work. Scheduler finds ready steps and publishes dispatch after durable commit.

## 49. Transactional outbox

Persist state transition and event atomically, then publish asynchronously and mark delivery.

## 50. Outbox recovery

On restart, scan unpublished records. Duplicate publication is acceptable because consumers are idempotent.

## 51. Worker lease

Claim with lease expiry and fencing token. Heartbeat extends ownership within limits.

## 52. Fencing token

Every state-changing commit checks current token, preventing a recovered stale worker from overwriting newer results.

## 53. Step attempts

Each retry creates an immutable attempt record with worker, image, start/end, error, artifacts and external IDs.

## 54. Idempotency key

Scope by tenant/run/step/action-version and store canonical request hash. Same key with different hash is a hard conflict.

## 55. Ambiguous external result

Timeout after a side effect transitions to UNKNOWN. Reconciliation queries provider state before retry.

## 56. Reconciliation service

Continuously resolves UNKNOWN and orphaned external tasks, using provider IDs/idempotency keys and evidence.

## 57. Retry classifier

Distinguish validation, policy, transient transport, provider throttle, capacity and permanent failures.

## 58. Retry budget

Bound retries per step/run/provider to avoid retry storms and runaway GPU/model cost.

## 59. Circuit breaker

Open on sustained provider/tool failure; fail fast or queue rather than amplifying outage.

## 60. Bulkhead isolation

Separate research, code, tests, GPU simulation, reconciliation and interactive workloads.

## 61. Backpressure

Control queue age, concurrent runs, fan-out, GPU jobs, model calls, tool calls and artifact throughput.

## 62. Priority

Combine business priority with aging and fairness; never let high priority bypass security or approval.

## 63. Fairness

Use tenant/team weighted fairness so one large engineering campaign does not monopolize GPU capacity.

## 64. Cancellation

Persist cancellation intent and propagate to queue, sandbox, GPU scheduler, MCP/A2A tasks and evaluator.

## 65. Compensation

For reversible external engineering actions, define explicit compensation; never call it database rollback.

## 66. Approval service

Store exact action, action hash, risk, evidence, requester, required role, expiry and decision.

## 67. Approval substitution defense

Any material change to target repo/branch/diff/deploy parameters changes the hash and requires fresh approval.

## 68. Separation of duties

For sensitive merges/deployments, authoring agent/requester cannot be sole approver.

## 69. Human input

Missing requirements move the run to WAITING_INPUT; the response is a durable event and may trigger a new plan version.

## 70. Plan versioning

Replan creates a new immutable version and reuses only still-valid completed artifacts.

## 71. Repair loop

Evaluator requests a bounded targeted repair with explicit failing criterion rather than unconstrained self-editing.

## 72. Infinite-loop controls

Cap plan versions, repairs, steps, model calls, tool calls, GPU minutes, wall time and cost.

## 73. Working memory

Ephemeral current execution context reconstructed from durable state when possible.

## 74. Session memory

Short-lived interaction continuity scoped to user/project/session.

## 75. Episodic memory

Prior investigations and outcomes with timestamps, provenance and retention.

## 76. Semantic memory

Authorized code/docs retrieval; semantic index is not source of truth.

## 77. Entity memory

Repositories, commits, issues, services, kernels, datasets, experiments and hardware entities.

## 78. Procedural memory

Reviewed engineering conventions and workflow preferences, never security authority.

## 79. Memory write gate

Classify candidate memory, verify provenance, scope, retention, sensitivity and conflicts before persistence.

## 80. Memory poisoning defense

Low-trust content cannot silently become durable procedure or high-confidence knowledge.

## 81. Repository authorization

Apply repo/path/branch authorization before code enters retrieval or model context.

## 82. Secret scanning

Scan prompts, diffs, logs and artifacts; redact or block credentials before external model/tool transmission.

## 83. Prompt injection defense

README, issues, logs, webpages and code comments are untrusted data; embedded instructions do not alter authority.

## 84. Tool injection defense

Tool admission is administrative; a model cannot dynamically add an arbitrary executable tool.

## 85. SSRF defense

Validate DNS/IP and redirects, block private/metadata destinations unless explicitly approved, and enforce egress policy.

## 86. Dependency security

Pin dependencies, verify hashes/signatures, generate SBOM and scan images/packages.

## 87. Sandbox escape defense

Patch runtime/kernel, minimize capabilities, isolate namespaces and continuously test escape boundaries.

## 88. Model gateway

Centralize model providers, data policy, prompt versions, token budgets, rate limits, fallback and telemetry.

## 89. Model selection

Route by coding/reasoning quality, context, privacy, latency, cost, region and availability.

## 90. Model fallback

Fallback cannot weaken privacy, residency or security classification.

## 91. Prompt registry

Version planner, debugger, reviewer and evaluator prompts and attach exact versions to attempts.

## 92. Evaluation layers

Use schema validation, deterministic tests, static/security checks, benchmarks, model critique and human acceptance.

## 93. Correctness before speed

Optimization is rejected if functional/numerical correctness fails, regardless of benchmark gain.

## 94. Independent evaluation

Where practical, use a separate evaluator configuration from the code-generating agent.

## 95. Golden regression corpus

Maintain representative bugs/performance cases to compare planner/agent versions.

## 96. Offline agent evaluation

Measure success, tool selection, repair count, policy compliance, cost and latency on a frozen corpus.

## 97. Online agent evaluation

Track acceptance, escaped defects, rollback, time-to-diagnosis and verified performance improvement.

## 98. Observability trace

Propagate trace context across API, event bus, model gateway, MCP and sandbox execution.

## 99. Structured logs

Log IDs, states, versions and error classes; avoid raw source/secrets/customer data by default.

## 100. Metrics cardinality

Workflow/repo IDs belong in traces/logs, not high-cardinality metric labels.

## 101. Platform metrics

Queue age, dispatch latency, step duration, retries, UNKNOWN, reconciliation, approval wait and sandbox failures.

## 102. GPU metrics

Utilization, memory, allocation wait, job duration, failure/preemption and cost.

## 103. Quality metrics

Test pass, benchmark significance, repair/replan rate, PR acceptance and rollback.

## 104. Audit model

Record actor, workload identity, repo/commit, capability, policy, tool, sandbox, artifact hashes and approval.

## 105. Multi-tenancy

Isolate SQL, queues, cache, artifacts, vector indexes, credentials, model routing, GPU quota, logs and traces.

## 106. Data residency

Keep source code, artifacts and model requests in allowed regions/providers.

## 107. Retention

Define separate retention for workflow state, source-derived artifacts, audit, memory, traces and sandbox snapshots.

## 108. Deletion

Delete from SQL, object store, semantic indexes, cache and derived memory according to policy.

## 109. Database schema

Use runs, plan_versions, steps, attempts, leases, approvals, idempotency, outbox, artifacts, skills, sandboxes and audit.

## 110. Database indexes

Index runnable steps, leases, unpublished outbox, pending approvals, UNKNOWN steps and run event time.

## 111. SQL transactions

Keep transactions short; never hold them across model, MCP, Git, CI or GPU calls.

## 112. Isolation level

Use serializable/retry-safe patterns where invariants require it; avoid hot global counters.

## 113. Redis

Use for cache, rate limits and ephemeral coordination, never as sole durable workflow truth.

## 114. Kafka/Pulsar

Use for dispatch/events with idempotent consumers; SQL remains queryable source of truth.

## 115. Object storage

Use immutable object keys, encryption, tenant authorization, integrity hash and lifecycle policies.

## 116. Alembic migrations

Production uses reviewed expand/contract migrations, not startup create_all.

## 117. Kubernetes control plane

Deploy API, planner, scheduler, approval, reconciliation, registry and gateways separately.

## 118. Kubernetes worker plane

Separate CPU, code-test, profiler, simulation and GPU worker pools with topology/resource constraints.

## 119. NetworkPolicy

Allow only explicit control-plane, artifact, inference and tool destinations.

## 120. Workload identity

Pods/services authenticate with short-lived workload identities rather than shared API keys.

## 121. Autoscaling

Scale by queue age, pending GPU requests, active sandboxes and utilization, not CPU alone.

## 122. Multi-region

Assign one authoritative execution region per step and fence the old region during failover.

## 123. DR

Restore authoritative state, replay outbox, reconcile external actions, validate artifacts and resume safe work.

## 124. RPO/RTO

Define separate objectives for workflow state, audit, artifacts and memory.

## 125. Capacity model

Estimate goals/day × steps/goal × attempts plus GPU-minute distribution and artifact bandwidth.

## 126. Cost accounting

Persist model tokens, CPU/GPU seconds, storage, tool/API and egress cost per run.

## 127. Budget enforcement

Planner sees budget; runtime enforces it independently.

## 128. CI pipeline

Lint, unit, property, contract, integration, SAST, dependency/SBOM, image/signature, sandbox and load tests.

## 129. Property tests

Prove dependency ordering, tenant isolation, approval safety, idempotency and fencing invariants.

## 130. Contract tests

Validate MCP/OpenShell/provider request/response, auth, timeouts, errors, cancellation and versions.

## 131. Load tests

Exercise many small investigations, giant DAGs, GPU backlogs, approval queues and post-outage bursts.

## 132. Chaos tests

Kill workers, duplicate events, fail DB, restart gateways, timeout models/tools and remove Redis.

## 133. Security tests

Test malicious repository instructions, credential exfiltration, SSRF, tool abuse and sandbox escape attempts.

## 134. SLOs

Separate API/durable-acceptance/scheduler SLOs from long-running engineering completion objectives.

## 135. Dashboard

Show active runs, queue age, GPU backlog, connector health, retries, UNKNOWN, approval backlog, quality and cost.

## 136. Alerting

Alert on sustained queue age, reconciliation backlog, sandbox failures, DB saturation, GPU starvation and policy anomalies.

## 137. Incident: stuck run

Find oldest nonterminal step, inspect lease/worker/provider/approval, reconcile UNKNOWN, and only requeue safely.

## 138. Incident: tool outage

Open circuit, stop retry amplification, preserve durable work, recover gradually and reconcile writes.

## 139. Incident: compromised skill

Disable version, revoke credentials, quarantine sandboxes/artifacts, inspect audit and require reviewed replacement.

## 140. Incident: sandbox vulnerability

Stop new sandbox creation for affected image/runtime, drain/isolate, patch, rebuild and validate.

## 141. Application: GPU regression

Detect -> reproduce -> profile -> diagnose -> patch -> test -> benchmark -> review -> PR.

## 142. Application: CUDA optimization

Baseline -> profiler -> kernel/config hypothesis -> candidate -> correctness -> benchmark.

## 143. Application: dataframe acceleration

Identify dataframe hotspot -> cuDF-style candidate -> semantic equivalence -> performance comparison.

## 144. Application: optimization solver

Formulate constraints/objective -> cuOpt-style solve -> validate feasibility -> compare objective.

## 145. Application: physical simulation

Prepare PhysicsNeMo-style spec -> GPU sandbox -> simulation -> validation -> artifact/report.

## 146. Application: quantum experiment

Prepare CUDA-Q-style experiment -> policy/cost gate -> execution -> statistical validation.

## 147. Application: autonomous bug repair

Reproduce -> diagnose -> candidate diff -> isolated tests -> independent review -> approval.

## 148. Application: dependency upgrade

Assess compatibility/security -> isolated upgrade -> tests/benchmarks -> migration notes -> PR.

## 149. Application: CI failure triage

Ingest failing job -> evidence -> root cause -> repair candidate -> rerun exact CI environment.

## 150. Application: performance PR review

Run controlled baseline/candidate benchmarks and attach evidence to review.

## 151. Local mock mode

Runs end-to-end without NVIDIA credentials or GPU and clearly labels simulated sandbox/tool responses.

## 152. Real integration mode

Requires installed/approved NVIDIA stack, hardware, credentials, policy and provider-specific adapters.

## 153. Code: domain.py

Typed GoalRequest, StepSpec and Plan define the control-plane contract.

## 154. Code: planner.py

Deterministic planner keeps local demo reproducible; production model planner must emit the same schema.

## 155. Code: compiler.py

Validates graph uniqueness/dependencies/acyclicity.

## 156. Code: skills.py

Bounds agent capabilities and associates risk.

## 157. Code: agents.py

Implements specialist-agent reference behavior.

## 158. Code: sandbox.py

Defines the OpenShell-compatible execution boundary and mock/live modes.

## 159. Code: mcp.py

Defines MCP gateway call boundary and mock/live modes.

## 160. Code: policy.py

Implements deterministic risk decisions independent of model reasoning.

## 161. Code: runtime.py

Executes dependency-ready steps, routes sandbox/MCP/evaluation and enforces approval.

## 162. Code: evaluator.py

Returns PASS/REPAIR based on structured results; production extends criteria.

## 163. Code: security.py

Local API-key authentication plus canonical action hashing.

## 164. Code: models.py

Defines durable run/step/approval/idempotency/outbox/audit foundations.

## 165. Code: memory.py

Implements six memory namespaces as an extension point.

## 166. Code: service.py

Coordinates goal -> plan -> execution.

## 167. Code: api.py

Exposes skills, goal execution and direct typed-plan execution.

## 168. Code: main.py

Bootstraps FastAPI and local schema.

## 169. Production code gap

The local runtime is primarily in-process; full production requires wiring SQL transitions, outbox publisher, event bus, workers, approval resume and reconciliation.

## 170. Upgrade phase 1

Enterprise OIDC, trusted tenant/repo identity, Alembic and persistent run/step transitions.

## 171. Upgrade phase 2

Outbox publisher, Kafka/Pulsar, scheduler, workers, leases/fencing and idempotency.

## 172. Upgrade phase 3

Production OpenShell/NemoClaw lifecycle, MCP gateway, credential broker and artifact service.

## 173. Upgrade phase 4

GPU scheduler, real NVIDIA SDK adapters, persistent memory, model gateway and evaluation service.

## 174. Upgrade phase 5

OTel, Kubernetes, multi-region, load/chaos/security/DR certification.

## 175. Principal framing

Explain why probabilistic reasoning is separated from deterministic policy, durable state, isolation and evidence.

## 176. Design tradeoff: DAG

DAGs simplify dependency reasoning and parallelism; dynamic workflows need versioned replanning rather than hidden mutation.

## 177. Design tradeoff: SQL + queue

SQL provides authoritative queryable state; queue provides scalable asynchronous delivery.

## 178. Design tradeoff: sandbox

Isolation costs startup/resources but is necessary because generated code and autonomous agents are untrusted.

## 179. Design tradeoff: human approval

Approval adds latency but creates a clear authority boundary for PR/merge/deploy and expensive operations.

## 180. Final invariant

No model output alone can authorize a consequential action, bypass isolation, establish provider success or overwrite durable truth.


# Complete local runbook

## Prerequisites

```text
Docker + Docker Compose
or
Python 3.11+
PostgreSQL 16
Redis 7
```

GPU/NVIDIA SDKs are **not required** for mock mode.

## Docker

```bash
unzip nvidia-autonomous-ai-engineer-platform-comprehensive.zip
cd nvidia-autonomous-ai-engineer-platform
cp .env.example .env
docker compose build
docker compose up -d
docker compose ps
curl http://localhost:8000/health
```

## List skills

```bash
curl http://localhost:8000/v1/skills \
  -H 'x-api-key: change-me'
```

## Run included autonomous engineering goal

```bash
curl -X POST http://localhost:8000/v1/goals \
  -H 'x-api-key: change-me' \
  -H 'Content-Type: application/json' \
  --data-binary @examples/goal.json
```

Expected high-level flow:

```text
research
 -> diagnose
 -> patch
 -> unit test in sandbox
 -> profile in sandbox
 -> evaluate
 -> WAITING_APPROVAL
 -> PR blocked until approved
```

## OpenAPI

```text
http://localhost:8000/docs
```

## Host development

```bash
docker compose up -d postgres redis

python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Change the PostgreSQL/Redis hosts in `.env` from container names to `localhost`, then:

```bash
uvicorn app.main:app --reload
```

## Tests

```bash
pytest -q
ruff check .
```

## Database

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

## Logs

```bash
docker compose logs -f api
docker compose logs -f postgres
docker compose logs -f redis
```

## Stop

```bash
docker compose down
```

Delete local volumes only when intentionally resetting local state:

```bash
docker compose down -v
```

# Production state model

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

# Transaction boundary

```text
BEGIN
  claim/update durable step
  insert audit
  insert outbox
COMMIT

perform model/tool/sandbox/GPU call

BEGIN
  verify fencing token
  persist result/artifact references
  insert next outbox events
COMMIT
```

Never keep the SQL transaction open across the external call.

# Principal-level system-design summary

```text
Engineering Goal
      |
Identity + Constraints
      |
Planner / Model Gateway
      |
Typed Plan
      |
Compiler + Skill Registry
      |
Policy
      |
Distributed SQL
      |
Outbox -> Kafka/Pulsar
      |
Scheduler
      |
CPU/GPU Workers
      |
OpenShell Sandbox + MCP Gateway
      |
CUDA / cuDF / cuOpt / PhysicsNeMo / CUDA-Q / Git / CI
      |
Artifacts + Evidence Graph
      |
Evaluator
      |
PASS / REPAIR / REPLAN
      |
Human Approval
      |
PR / Existing CI-CD
      |
Audit + OTel + Outcome Feedback
```

# Production-readiness checklist

```text
[ ] OIDC/workload identity
[ ] repository/path authorization
[ ] Alembic migrations
[ ] persisted run/step/attempt transitions
[ ] transactional outbox publisher
[ ] Kafka/Pulsar
[ ] scheduler/workers
[ ] leases/fencing
[ ] idempotency
[ ] UNKNOWN/reconciliation
[ ] approval decision + resume
[ ] cancellation/compensation
[ ] production OpenShell/NemoClaw lifecycle integration
[ ] managed MCP
[ ] credential broker
[ ] signed skill/image/SBOM
[ ] GPU scheduler/quota
[ ] real NVIDIA SDK adapters required by workload
[ ] artifact/object storage
[ ] persistent governed memory
[ ] model gateway
[ ] OTel/metrics/logs/audit export
[ ] Kubernetes/NetworkPolicy
[ ] load/chaos/security/sandbox tests
[ ] backup/restore/DR
```

# Important implementation boundary

This package is an independent, runnable, production-oriented **reference implementation**, not NVIDIA proprietary source. The local path intentionally uses mock NVIDIA/OpenShell/MCP responses where real execution would require NVIDIA software, compatible GPUs, organization credentials, policies and infrastructure. The documentation explicitly identifies these integration points rather than fabricating them.

# Final design rule

```text
Model        -> proposes
Planner      -> structures work
Compiler     -> validates
Policy       -> authorizes
SQL          -> owns durable truth
Scheduler    -> dispatches
Skills/MCP   -> expose bounded capability
OpenShell    -> contains untrusted execution
GPU runtime  -> runs controlled experiments
Evaluator    -> verifies evidence
Approval     -> controls consequential actions
Audit        -> reconstructs the lifecycle
```

The system trusts evidence and durable state, not an agent's assertion that work succeeded.
