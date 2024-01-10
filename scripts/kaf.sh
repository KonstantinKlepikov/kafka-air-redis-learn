#! /usr/bin/env sh

# Exit in case of error
set -e

INSTALL_DEV=true \
docker compose \
-f docker-compose.kaf.yml \
config > docker-stack-kaf.yml

docker compose -f docker-stack-kaf.yml build
docker compose -f docker-stack-kaf.yml down --remove-orphans
docker compose -f docker-stack-kaf.yml up -d
