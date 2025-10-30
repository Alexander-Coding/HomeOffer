FROM python:3.12-alpine

WORKDIR /app

RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev

RUN pip install uv

COPY pyproject.toml ./

RUN uv venv

RUN uv sync

COPY . .

EXPOSE 8080

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "1"]
