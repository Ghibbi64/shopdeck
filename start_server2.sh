#!/bin/bash

source .venv/bin/activate
flask --app main run --cert ./0.0.0.0.pem --key ./0.0.0.0-key.pem -h 0.0.0.0 -p 8000 --debug
