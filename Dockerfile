FROM python:3.10-slim AS builder

WORKDIR /app
COPY util.py .

FROM python:3.10-alpine

WORKDIR /app
COPY --from=builder /app/util.py .

ENTRYPOINT ["python", "util.py"]
