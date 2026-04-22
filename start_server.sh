#!/bin/bash

source .venv/bin/activate
python manage.py runserver_plus --cert-file ./192.168.1.1.pem --key-file ./192.168.1.1-key.pem 192.168.1.1:9000
