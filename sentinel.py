import time
import os
import subprocess

TARGET_LATCH = 0.00016
LOG_DIR = "/sdcard/Black_Stallion/logs"
REPORT_DIR = "/sdcard/Black_Stallion/reports"

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

def generate_mobile_report(drift, context):
    ts = time.strftime("%Y%m%d_%H%M%S")
    with open(f"{REPORT_DIR}/Mobile_Vuln_{ts}.md", "w") as f:
        f.write(f"# MOBILE VULN\nDrift: {drift:.8f}s\n\nContext:\n{context}")
    print("\033[93m[!] VULN ARCHIVED\033[0m")

print("\033[92m[+] Mobile Sentinel Active. Latching to .16ms...\033[0m")

while True:
    start = time.monotonic()
    _ = [x for x in range(1000)]
    drift = time.monotonic() - start

    if drift > TARGET_LATCH:
        try:
            with open(f"{LOG_DIR}/drift.log", "a") as f:
                f.write(f"{time.ctime()} | DRIFT: {drift:.8f}s\n")
        except IOError:
            pass

        if drift > 0.001:
            try:
                ctx = subprocess.check_output(['top', '-n', '1', '-b']).decode()
                generate_mobile_report(drift, ctx)
            except Exception:
                generate_mobile_report(drift, "Failed to capture execution context tree.")
    time.sleep(0.001)
