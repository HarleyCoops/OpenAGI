# Learning path for orchestrating agents

Use this path to move from high-level understanding to hands-on experiments. Pair each step with the linked documentation and the templates in `docs/templates/`.

1. **Orientation**
   - Read the documentation landing page to understand the platform goals and terminology.
   - Capture your own glossary using `docs/templates/concept-overview.md`.

2. **Environment setup**
   - Note authentication, SDK installation, and CLI prerequisites from the docs.
   - Write down the commands, required environment variables, and any troubleshooting tips in `docs/templates/setup-log.md`.

3. **Hello-world agent**
   - Identify the simplest example in the docs (creating and running a single agent).
   - Reproduce it in `examples/` (e.g., a small script or notebook) and annotate decisions in `docs/templates/run-journal.md`.

4. **Multi-agent orchestration**
   - Focus on how agents coordinate: messaging, task routing, and state sharing.
   - Sketch the control flow in `docs/templates/orchestration-walkthrough.md`, then implement a minimal orchestration example in `examples/`.

5. **Tools and integrations**
   - Track how agents call external tools or APIs. List required scopes, payload shapes, and error patterns.
   - Document findings in `docs/templates/tooling-checklist.md`.

6. **Observability and evaluation**
   - Look for logging, tracing, and evaluation guidance in the docs.
   - Record which signals to capture and how to visualize them in `docs/templates/observability-plan.md`.

7. **Hardening and deployment**
   - Summarize best practices for productionizing agents (rate limits, retries, privacy, security, and cost controls).
   - Capture deployment steps and rollback plans in `docs/templates/deployment-plan.md`.

8. **Retrospective**
   - After each experiment, log what worked and what confused you in `docs/templates/retro.md`.
   - Convert successful experiments into concise, well-commented examples under `examples/`.

9. **Applied use case: TillerHQ login agent**
   - Walk through the computer-use flow in `docs/use-cases/tiller-login.md`.
   - Run the scaffold in `examples/computer_use/tiller_login.py` and adapt it to the Lux SDK planning APIs.

> Tip: Keep each step small. The goal is to transform passive reading into runnable, reproducible experiments.
