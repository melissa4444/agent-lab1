# Agent Lab 1

Lab 1: load an OpenAI API key, run a few chat calls, and chain prompts together.

## Lab summary
This lab introduces the basic pattern of an AI workflow: send a prompt to an LLM, use its output as input for another step, and evaluate the result. The project is a small, standalone example built with Python and the OpenAI API.

The script starts by asking the model for a fun fact, then creates a difficult question, answers it, and finally judges whether that answer is correct. This demonstrates prompt chaining, where intermediate outputs are passed between model calls to create a simple reasoning pipeline.

It is designed as a beginner-friendly exercise in working with environment variables, configuring an API key, and building a minimal “agent-like” workflow in code.


## Setup

```bash
cd ~/projects/agent-lab1
uv sync
cp .env.example .env
```

Edit `.env` and paste your OpenAI API key after `OPENAI_API_KEY=`.

## Run

**Notebook:** open `lab1.ipynb`, select the `.venv` kernel, and run cells with Shift+Enter.

**Script:**

```bash
uv run lab1.py
```


