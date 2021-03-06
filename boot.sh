#!/bin/bash -e

if [ -f venv/bin/activate ]; then
    echo   "Load Python virtualenv from '.venv/bin/activate'"
    source venv/bin/activate
fi
exec "$@"

export RUN_MODE=production
gunicorn -b 0.0.0.0:5054 --threads 4 --access-logfile - --error-logfile - SMARTHOME_NODE:app

# -b or --bind=x.x.x.x:num = bind ip and port
# --log-level debug = For gunicorn debug
# -w 4 = To add 4 workers. This should be between 4-12
# --threads = Add number of threads to each worker
