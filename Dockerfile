FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV DB_PATH=/data/tasks.db

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /data

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:${PORT:-5000} app:app
