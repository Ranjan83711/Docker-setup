FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

COPY california1.joblib .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "california_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]

