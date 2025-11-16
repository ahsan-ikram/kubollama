# Use lightweight Python image
FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/
COPY src /app/src

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install --no-root

# Add src to Python path
ENV PYTHONPATH=/app/src

CMD ["poetry", "run", "python", "-m", "ollama_client.main"]