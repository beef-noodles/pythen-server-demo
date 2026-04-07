FROM python:3.14-slim as builder

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

FROM python:3.14-slim
WORKDIR /app
COPY --from=builder /usr/bin/curl /usr/bin/curl
COPY --from=builder /bin/uv /usr/bin/uv

ENV PYTHONUNBUFFERED True
COPY . .
RUN uv pip install --system -r requirements.txt

ENTRYPOINT [ "bash", "./startup.sh" ]
