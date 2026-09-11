#!/bin/bash
# Evidence Harvester - Metric Aggregator Core
VAULT_DIR="$HOME/Apple-Router-Sentinel/artifacts"
LOCKER_DIR="$HOME/Apple-Router-Sentinel/evidence_locker"

mkdir -p "$VAULT_DIR" "$LOCKER_DIR"

echo -e "\033[94m[*] HARVESTER ACTIVE: Compiling runtime timing statistics...\033[0m"

# Safely dump process drifts into the log boundary
if [ -f /sdcard/Black_Stallion/logs/drift.log ]; then
    cat /sdcard/Black_Stallion/logs/drift.log >> "$VAULT_DIR/network_blocks.log" 2>/dev/null
    echo -e "\033[92m[+] Successfully synchronized local mobile drift profiles.\033[0m"
else
    echo "Iteration,Delta_Ticks" > "$VAULT_DIR/network_blocks.log"
fi
