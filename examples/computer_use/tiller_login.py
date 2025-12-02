"""End-to-end scaffold for a computer-use agent that signs in to TillerHQ.

The script mirrors the Lux SDK flow: build a system prompt, request a plan,
then execute it. The planning call is stubbed so you can run locally today and
swap in the SDK later.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from playwright.async_api import Browser, Page, async_playwright


@dataclass
class AgentConfig:
    email: str
    password: str
    mfa_code: Optional[str]
    headless: bool = True
    screenshots_dir: Path = Path("screenshots")


@dataclass
class PlannedAction:
    action: str
    selector: Optional[str] = None
    url: Optional[str] = None
    value: Optional[str] = None
    timeout_ms: Optional[int] = None


LOGIN_URL = "https://sheets.tillerhq.com/login"


def load_config(headless: bool) -> AgentConfig:
    email = os.environ.get("TILLER_EMAIL")
    password = os.environ.get("TILLER_PASSWORD")
    mfa_code = os.environ.get("TILLER_MFA_CODE")

    missing = [name for name, val in {"TILLER_EMAIL": email, "TILLER_PASSWORD": password}.items() if not val]
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

    cfg = AgentConfig(email=email, password=password, mfa_code=mfa_code, headless=headless)
    cfg.screenshots_dir.mkdir(parents=True, exist_ok=True)
    return cfg


def build_lux_prompt(config: AgentConfig) -> str:
    """Construct the system prompt you would send to the Lux SDK."""
    return (
        "You are a focused computer-use agent whose only task is to sign in to TillerHQ.\n"
        "Constraints:\n"
        f"- Only navigate to the official login page: {LOGIN_URL}.\n"
        "- Fill the email, password, and backup code fields with provided secrets.\n"
        "- Click the login / submit buttons when appropriate.\n"
        "- Stop after the account home/dashboard finishes loading and report success.\n"
        "- Do not attempt any financial actions.\n"
    )


def draft_plan_with_lux(config: AgentConfig) -> List[PlannedAction]:
    """Return a static plan placeholder to be replaced by a Lux SDK call.

    Replace this function with the actual SDK request once available locally,
    parsing the returned JSON into ``PlannedAction`` entries.
    """

    plan: List[PlannedAction] = [
        PlannedAction(action="goto", url=LOGIN_URL),
        PlannedAction(action="fill", selector="input[type=email]", value=config.email),
        PlannedAction(action="fill", selector="input[type=password]", value=config.password),
        PlannedAction(action="click", selector="button[type=submit]"),
        PlannedAction(action="maybe_fill", selector="input[name=backupCode]", value=config.mfa_code),
        PlannedAction(action="wait_for", selector="[data-test-id=dashboard]", timeout_ms=10000),
    ]
    return plan


async def execute_plan(actions: List[PlannedAction], config: AgentConfig) -> None:
    async with async_playwright() as p:
        browser: Browser = await p.chromium.launch(headless=config.headless)
        page: Page = await browser.new_page()

        for step in actions:
            if step.action == "goto" and step.url:
                print(f"[navigate] {step.url}")
                await page.goto(step.url)
            elif step.action == "fill" and step.selector:
                print(f"[fill] {step.selector}")
                await page.fill(step.selector, step.value or "")
            elif step.action == "maybe_fill" and step.selector and step.value:
                print(f"[maybe_fill] {step.selector}")
                await page.fill(step.selector, step.value)
            elif step.action == "click" and step.selector:
                print(f"[click] {step.selector}")
                await page.click(step.selector)
            elif step.action == "wait_for" and step.selector:
                print(f"[wait_for] {step.selector}")
                await page.wait_for_selector(step.selector, timeout=step.timeout_ms or 5000)
            else:
                print(f"[skip] Unrecognized or incomplete step: {step}")

        screenshot_path = config.screenshots_dir / "tiller_login.png"
        await page.screenshot(path=screenshot_path, full_page=True)
        print(f"[done] Saved screenshot to {screenshot_path}")
        await browser.close()


def serialize_plan(actions: List[PlannedAction]) -> str:
    return json.dumps([action.__dict__ for action in actions], indent=2)


async def main() -> None:
    parser = argparse.ArgumentParser(description="Run the TillerHQ login computer-use agent")
    parser.add_argument("--headful", action="store_true", help="Launch Chromium in headed mode")
    args = parser.parse_args()

    config = load_config(headless=not args.headful)
    prompt = build_lux_prompt(config)
    plan = draft_plan_with_lux(config)

    print("=== System prompt (send to Lux SDK) ===")
    print(prompt)
    print("=== Planned actions ===")
    print(serialize_plan(plan))

    await execute_plan(plan, config)


if __name__ == "__main__":
    asyncio.run(main())
