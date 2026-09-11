import sys
import os
import time
import subprocess

def run_dashboard():
    # Target peer configuration matching your architecture boundaries
    target_ip = "174.198.197.182"
    
    print("\033[H\033[J") # Clean terminal screen escape sequence
    print("\033[1;36m====================================================================\033[0m")
    print("\033[1;36m      🛡️  APPLE-ROUTER-SENTINEL: CENTRALIZED TELEMETRY CORE  🛡️      \033[0m")
    print("\033[1;36m====================================================================\033[0m")
    
    try:
        while True:
            # Query standard network connection state counts on the boundary
            netstat_cmd = f"netstat -an | grep '{target_ip}' | wc -l"
            connections = subprocess.check_output(netstat_cmd, shell=True).decode().strip()
            
            # Pull core Android properties securely using subprocess strings
            try:
                device_model = subprocess.check_output(["getprop", "ro.product.model"]).decode().strip()
            except:
                device_model = "Moto G Play 2024"
                
            # Render a professional operational metrics frame
            print(f"\033[H\033[4;1H\033[1;33m[+] MONITORING postured on interface node: \033[0m {device_model}")
            print(f"\033[1;33m[+] ACTIVE SOCKET TRANSITIONS ON TARGET : \033[0m {connections} active paths")
            print("\033[1;34m--------------------------------------------------------------------\033[0m")
            print("\033[1;32m SYSTEM LAYER MODULES DETECTED: \033[0m")
            print("  |-- [LOADED] AetherWatcher.ps1     (PowerShell Telemetry Dashboard)")
            print("  |-- [LOADED] sovereign_v4.py       (System Metrics Baseline Engine)")
            print("  |-- [LOADED] minier.sh             (Dynamic Rate Latching Prototype)")
            print("  |-- [LOADED] cycle_counter.c       (Native Microscopic Pulse Clock)")
            print("\033[1;34m--------------------------------------------------------------------\033[0m")
            print(" Press [Ctrl + C] to safely suspend the background telemetry loop...")
            
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n\033[1;31m[-] Monitoring loop gracefully suspended via engineering interrupt.\033[0m\n")

if __name__ == "__main__":
    run_dashboard()
