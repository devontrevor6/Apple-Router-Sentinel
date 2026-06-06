#!/data/data/com.termux/files/usr/bin/bash
VAULT_TARGET=~/Apple-Router-Sentinel/artifacts
while true; do
    if [ -d "$VAULT_TARGET" ]; then
        NEW_INTEL=$(find "$VAULT_TARGET" -type f -cmin -1 | grep -v "sentinel")
        if [ ! -z "$NEW_INTEL" ]; then
            termux-notification -c "MALICIOUS ACTIVITY DETECTED" -t "Sentinel found new intel"
            termux-vibrate -d 500
        fi
    fi
    sleep 60
done
