# OpenAGI Learning Playground

This repository is a lightweight, easy-to-set-up companion for studying the agent orchestration concepts described in the [OpenAGI developer documentation](https://developer.agiopen.org/docs/index?utm_source=landing_page&utm_medium=web&utm_campaign=take_me_to_lux_sdk).

The project focuses on **verbosely explaining each concept**, providing note-taking templates, and suggesting hands-on exercises so you can translate the documentation into runnable experiments.

## Quick start

1. **Clone the repo**
   ```bash
   git clone <this-repo-url>
   cd OpenAGI
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. **Install tooling for notebooks and linting (optional)**
   The repo currently ships without external dependencies. If you want to capture experiments, install a minimal toolchain:
   ```bash
   python -m pip install --upgrade pip
   pip install jupyter black
   ```

## Repository layout

- `docs/` — Learning path, concept overviews, and templates you can fill in while reading the docs.
- `examples/` — Runnable code samples built from the docs.
  - `examples/computer_use/` — Scaffold for a Lux-aligned computer-use agent that logs into TillerHQ.
- `notes/` — Personal scratch space for experiments and observations (gitignored by default so you can jot freely).

## How to use this repo with the docs

1. Open the documentation link above in your browser.
2. Pick a topic from the learning path in `docs/learning-path.md`.
3. Copy the relevant template from `docs/templates/` into `notes/` and fill it with summaries, screenshots, or code snippets you derive from the docs.
4. Translate the concepts into runnable scripts or notebooks inside `examples/`, then record what you tried in the corresponding template.
5. Iterate until each concept has a **narrative explanation** and a **hands-on artifact**.

## Contributing

- Feel free to expand the templates with the actual API shapes you find in the docs.
- Keep examples minimal and well-commented so newcomers can follow along without deep prior knowledge.
- When you add runnable code, document how to execute it and include expected outputs.

Happy learning!
