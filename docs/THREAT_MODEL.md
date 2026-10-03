# Threat Model

Primary threats: malicious repository instructions, indirect prompt injection, secret exfiltration, unauthorized MCP calls, forged callbacks, dependency/supply-chain compromise, SSRF, sandbox escape, GPU denial of service, cross-tenant access, approval substitution, memory poisoning and excessive agency.

Core mitigations: deterministic authorization, OpenShell-style out-of-process policy, deny-by-default network/filesystem, credential brokerage, short-lived identity, signed artifacts/images, schema validation, action hashes, quotas, idempotency, reconciliation and immutable audit.
