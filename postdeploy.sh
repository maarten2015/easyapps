#!/bin/bash

set -e
set -o pipefail

python manage.py migrate
curl $SENTRY_DEPLOY_HOOK -X POST -H "Content-Type: application/json" -d "{\"version\": \"$CONTAINER_VERSION\"}"