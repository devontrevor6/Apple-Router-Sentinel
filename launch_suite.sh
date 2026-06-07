#!/bin/bash
echo "[*] Initializing Sentinel Suite..."
# Run the auditor in the background
./sentinel_activity &
# Start the telemetry server
python3 artifact_server.py &
# Alert if the log detects movement
echo "[*] Suite fully armed. Monitoring ingress..."
