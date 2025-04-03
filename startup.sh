#!/bin/bash
echo "start app..."
flask db upgrade
gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 "src:create_app()"
