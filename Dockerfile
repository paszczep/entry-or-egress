FROM ghcr.io/astral-sh/uv:python3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt ./

RUN uv pip install \
    --requirement requirements.txt \
    --system

COPY app/ app/

EXPOSE 8000

CMD ["uvicorn", "app.asgi:asgi_app", "--host", "0.0.0.0", "--port", "8000"]
