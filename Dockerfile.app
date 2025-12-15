# Use lightweight Python image
FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uv

# Create a virtual environment
RUN python -m venv .venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency definition and lock file
COPY pyproject.toml uv.lock ./

# Install dependencies from the lock file
RUN uv sync --no-dev

# Copy source code
COPY src /app/src

# Add src to Python path
ENV PYTHONPATH=/app/src

# Run the application
CMD ["python", "-m", "ollama_client.main"]