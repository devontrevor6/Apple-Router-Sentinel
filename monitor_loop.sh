#!/bin/bash
# Monitor loop with robust error handling
while true; do
  # Ensure log directory exists every time
  mkdir -p ./logs
  
  # Capture connections
  connections=$(netstat -an | grep ESTABLISHED | grep -v "127.0.0.1")
  
  if [ -n "$connections" ]; then
     echo "[!] ALERT: THREAT DETECTED at $(date)" >> ./logs/incident_report.txt
     echo "$connections" >> ./logs/incident_report.txt
  fi
  sleep 5
done
