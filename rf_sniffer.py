import subprocess, time, re
def get_rssi():
    try:
        cmd = "iw dev wlan0 scan dump"
        output = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT).decode()
        signals = re.findall(r"signal: (-?\d+) dBm", output)
        return max([int(s) for s in signals]) if signals else -100
    except: return -100
print("\033[91m[CRITICAL] RF INTERFERENCE AUDIT ACTIVE\033[0m")
print("Scanning for high-power anomalies...")
try:
    while True:
        rssi = get_rssi()
        if rssi > -30: status = "\033[41mDANGER: EXTREME POWER\033[0m"
        elif rssi > -45: status = "\033[93mWARNING: HIGH GAIN\033[0m"
        else: status = "\033[92mNORMAL\033[0m"
        print(f"{status} Peak Signal: {rssi} dBm", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n\033[94m[SYSTEM] Audit Logged to ~/Sovereign_Siege_PoC/\033[0m")
