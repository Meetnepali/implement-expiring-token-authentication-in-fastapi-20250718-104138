#!/bin/bash
set -e

printf '\n[*] Building Docker image...\n'
docker-compose build
printf '[*] Starting Docker containers...\n'
docker-compose up -d

printf '\n[*] Checking FastAPI service status...\n'
# Wait for the container to start up
for i in {1..10}
do
  if docker exec fastapi-customer-app curl -s http://localhost:8000/docs > /dev/null; then
    echo "[*] FastAPI service is up."
    exit 0
  else
    sleep 2
  fi
done

>&2 echo "[!] FastAPI API container did not become healthy in time. Check logs with 'docker-compose logs'."
exit 1
