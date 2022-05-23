# For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.8-slim
FROM python:3-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

RUN adduser -u 5678 --disabled-password --gecos "" app
RUN chown -R app /app
USER app

CMD ["python", "-m", "src"]
