FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY endpoints/ ./endpoints/
COPY tests/ ./tests/
COPY conftest.py .
CMD ["pytest", ".", "-v", "-s"]