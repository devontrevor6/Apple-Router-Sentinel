#!/bin/bash

# --- Pre-Flight Checks ---
if ! command -v python3 &> /dev/null; then
    echo "[!] ERROR: Python3 is not installed. Please install it to continue."
    exit 1
fi

if ! python3 -c "import flask" &> /dev/null; then
    echo "[!] ERROR: Flask library not found. Run 'pip install flask'."
    exit 1
fi

# 1. Kill any existing instances to clear the environment
pkill -f artifact_server.py
pkill -f sentinel_activity
pkill -f monitor_loop.sh

# 2. Wait 2 seconds for ports to clear
sleep 2

# 3. Setup environment
mkdir -p ./logs
chmod +x monitor_loop.sh

# 4. Launch with background protection
nohup python3 artifact_server.py > ./logs/server_logs.txt 2>&1 &
nohup ./monitor_loop.sh > ./logs/monitor_logs.txt 2>&1 &
./sentinel_activity &

echo "--------------------------------------------------------"
echo "Sentinel Suite is now active."
echo "View logs at: ./logs/server_logs.txt"
echo "--------------------------------------------------------"
