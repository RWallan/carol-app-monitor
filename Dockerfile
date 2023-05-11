FROM python:3.11-slim

# Disables Python buffering, causing output to be immediately displayed.
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip \
    && pip install poetry

RUN poetry export -f requirements.txt --output requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "carol_app_monitor/main.py"]
