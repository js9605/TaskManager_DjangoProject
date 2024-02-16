#!/bin/sh

# Apply database migrations
python TaskManager/manage.py migrate

# Start the main process
exec python TaskManager/manage.py runserver 0.0.0.0:8000
