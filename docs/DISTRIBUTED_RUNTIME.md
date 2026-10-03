# Distributed Runtime

SQL is authoritative. Scheduler commits READY plus outbox. Publisher sends to Kafka/Pulsar. Workers claim using leases/fencing, invoke sandbox/MCP/GPU workloads outside SQL transactions, persist immutable attempts/artifacts, and publish completion. Ambiguous external writes enter UNKNOWN and reconciliation.

Never rely on an in-memory coroutine as the only record of long-running engineering work.
