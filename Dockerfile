FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /code

COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen

COPY app ./app

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]