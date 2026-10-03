# Production Design

SQL is authoritative. Atomically persist state plus outbox, publish to Kafka/Pulsar, claim work using leases/fencing, run generated code in OpenShell-compatible sandboxes, record immutable artifacts/evidence, and reconcile ambiguous external writes. Never hold a DB transaction over model/tool/GPU calls.
