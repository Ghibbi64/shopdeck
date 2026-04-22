#!/bin/bash

source .venv/bin/activate
flask --app main run --cert ./192.168.1.1.pem --key ./192.168.1.1-key.pem -h 192.168.1.1 -p 8000 --debug
