#!/data/data/com.termux/files/usr/bin/bash
echo "[👑] HYPERVISOR WATCHDOG ACTIVE: DOUBLE TAP TO PURGE"
su -c "getevent -lt /dev/input/event1" | while read line; do
    if [[ "$line" == *"ABS_X"* || "$line" == *"ABS_Z"* ]]; then
        ((TAP_COUNT++))
    fi
    if [ "$TAP_COUNT" -eq 2 ]; then
        echo "[👑] SIGNAL RECEIVED: PURGING ALL CLOWN PROCESSES..."
        pkill -f python
        echo "[👑] GRID REBOOTED."
        TAP_COUNT=0
    fi
    (sleep 1 && TAP_COUNT=0) &
done
