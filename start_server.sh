#!/bin/bash

source .venv/bin/activate
python manage.py runserver_plus --cert-file ./0.0.0.0.pem --key-file ./0.0.0.0-key.pem 0.0.0.0:9000
