#!/bin/bash
set -e

bash ./install.sh

if docker ps | grep fastapi-customer-app > /dev/null; then
  echo "[*] FastAPI Customer API is running! Access it at http://localhost:8000/docs"
else
  echo "[!] Service failed to start. Check logs."
  exit 1
fi
