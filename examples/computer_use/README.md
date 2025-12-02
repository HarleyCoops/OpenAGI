# Computer-use agent: login to TillerHQ

This example turns the documentation-driven ideas in the repo into a runnable computer-use agent that signs in to [TillerHQ](https://tillerhq.com) on your behalf. It is intentionally verbose so you can trace every step from intent to execution.

The flow combines two parts:
- **Lux SDK (logic/agent)**: prompts and a simple loop structure you can wire up to the official SDK from the docs.
- **Playwright (computer control)**: concrete browser automation used to realize the agent's plan locally.

## Prerequisites
1. Python 3.10+
2. Install dependencies
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   playwright install chromium
   ```
3. Provide secrets via environment variables (keep these out of Git!):
   - `TILLER_EMAIL`
   - `TILLER_PASSWORD`
   - Optional: `TILLER_MFA_CODE` if your account prompts for a static backup code.
4. (Optional) `LUX_API_KEY` for wiring into the Lux SDK once available locally.

## What the agent does
1. Loads a **login-focused system prompt** that constrains scope to signing into TillerHQ.
2. Creates a **plan** (URL to open, fields to fill, buttons to click) using your future Lux client.
3. Executes the plan with **Playwright** so you can test locally without relying on remote automation.
4. Emits **structured logs** so you can plug the same plan into the official computer-use SDK later.

## Running locally
```bash
python examples/computer_use/tiller_login.py --headful   # set --headless to run quietly
```

Expected log outline:
- Sanitized configuration loaded
- Planned actions (URL, selectors, text)
- Browser steps (navigation, fills, clicks, screenshot path)

## Adapting to the Lux SDK
The `build_lux_prompt` and `draft_plan_with_lux` helpers mark the exact spots where you can call the SDK once installed. They currently return static content derived from the public TillerHQ login flow so you can iterate immediately.

Swap the stub in `draft_plan_with_lux` with a real SDK call that sends the plan request and parses the structured action list that the Lux docs describe.
