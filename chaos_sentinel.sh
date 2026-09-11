#!/bin/bash
# Chaos Sentinel - System Latency Stress Simulator
echo -e "\033[91m[!] INITIALIZING CHAOS SENTINEL INJECTION ENGINE...\033[0m"

while true; do
    # Generate controlled CPU spikes to monitor scheduler jitter variations
    dd if=/dev/urandom of=/dev/null bs=1M count=100 2>/dev/null
    sleep 0.5
done
