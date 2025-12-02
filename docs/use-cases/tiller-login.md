# Use case: computer-use agent that logs into TillerHQ

This walkthrough shows how to translate the Lux SDK's computer-use concepts into a concrete sign-in flow for TillerHQ.

## Goals
- Keep the agent narrowly scoped to **authentication** (no banking actions).
- Capture the **plan** as structured steps so it can be reused with or without the SDK.
- Make the flow reproducible locally with Playwright before delegating to hosted automation.

## Inputs and secrets
- `TILLER_EMAIL` / `TILLER_PASSWORD` (required)
- `TILLER_MFA_CODE` (optional backup code if prompted)
- `LUX_API_KEY` (optional; plug into the SDK when ready)

## System prompt sketch
```
You are a focused computer-use agent whose only task is to sign in to TillerHQ.
Constraints:
- Only navigate to the official login page: https://sheets.tillerhq.com/login.
- Fill the email, password, and backup code fields with provided secrets.
- Click the login / submit buttons when appropriate.
- Stop after the account home/dashboard finishes loading and report success.
- Do not attempt any financial actions.
```

## Planning shape
Ask the SDK for a concise action list like:
```
[
  {"action": "goto", "url": "https://sheets.tillerhq.com/login"},
  {"action": "fill", "selector": "input[type=email]", "value": "<email>"},
  {"action": "fill", "selector": "input[type=password]", "value": "<password>"},
  {"action": "click", "selector": "button[type=submit]"},
  {"action": "maybe_fill", "selector": "input[name=backupCode]", "value": "<mfa>"},
  {"action": "wait_for", "selector": "[data-test-id=dashboard]", "timeout_ms": 10000}
]
```

## Execution outline
1. Build the system prompt above.
2. Send a planning request via the Lux SDK with the sanitized secrets.
3. Execute the returned actions using either the SDK's computer control or Playwright.
4. Capture a screenshot and navigation log for traceability.

See `examples/computer_use/tiller_login.py` for an end-to-end scaffold that you can wire to the SDK.
