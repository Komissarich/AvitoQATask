FROM python:3.14-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY endpoints/ ./endpoints/
COPY tests/ ./tests/
COPY test_cases.yaml .
CMD ["pytest", ".", "-v", "-s"]