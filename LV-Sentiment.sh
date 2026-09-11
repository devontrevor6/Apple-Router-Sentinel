#!/bin/bash
LOG_FILE="./LV-Sentiment.log"
ps aux | awk '{print $2}' > .proc_baseline
while true; do
    ps aux | awk '{print $2}' > .proc_current
    NEW_PIDS=$(comm -13 .proc_baseline .proc_current)
    for pid in $NEW_PIDS; do
        NAME=$(ps -p $pid -o comm= 2>/dev/null)
        TIME=$(date +"%H:%M:%S")
        if [[ $NAME =~ (powershell|cmd|wmic|sh) ]]; then
            echo "$TIME | [CRITICAL] PROC-SPAWN | ID: $pid | $NAME" | tee -a "$LOG_FILE"
        else
            echo "$TIME | [INFO] PROC-SPAWN | ID: $pid | $NAME"
        fi
    done
    mv .proc_current .proc_baseline
    sleep 1
done
