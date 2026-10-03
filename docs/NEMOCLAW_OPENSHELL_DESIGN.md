# NemoClaw / OpenShell Integration Design

Production integration should treat NemoClaw as lifecycle/blueprint integration and OpenShell as the isolation and policy boundary. Pin compatible versions, validate host readiness, keep credentials outside sandboxes, use managed MCP for approved tools, preserve only manifest-declared state across snapshots/rebuilds, and fail closed on incompatible policy/runtime versions.

The local project uses an `OpenShell-compatible mock` so it remains runnable without installing NVIDIA software.
