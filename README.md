# Agent Lab 1

Standalone version of Lab 1: load an OpenAI API key, run a few chat calls, and chain prompts together.

## Setup

```bash
cd ~/projects/agent-lab1
uv sync
cp .env.example .env
```

Edit `.env` and paste your OpenAI API key after `OPENAI_API_KEY=`.

## Run

**Notebook:** open `lab1.ipynb` in Cursor, select the `.venv` kernel, and run cells with Shift+Enter.

**Script:**

```bash
uv run lab1.py
```

## Cursor kernel tip

If `.venv` doesn't appear as a kernel option: Settings → VS Code Settings → search `venv` → set **Path to folder with a list of Virtual Environments** to this project root (`/Users/m3l5/projects/agent-lab1`).
