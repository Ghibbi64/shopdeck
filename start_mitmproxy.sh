#!/bin/bash
source .venv/bin/activate
mitmweb \
  --set stream_large_bodies=500k \
  --web-host 0.0.0.0 \
  --set showhost=true \
  --listen-port 8888 \
  --set console_eventlog_verbosity=debug \
  --set termlog_verbosity=debug \
  --set tls_version_client_min=TLS1_1 \
  --set tls_version_server_min=TLS1_1 \
  --set client_certs=./ClCert.pem \
  --ssl-insecure \
  --allow-hosts '.*' \
  -s ./mitmproxy/rewrite_script.py \
  -s ./mitmproxy/rewrite_spotpass.py