#!/bin/bash
# G1 CHAOS SENTINEL - Local Active Response Module

TARGET_IP="174.198.197.182"
GATEWAY_IP=$(ip route show | grep default | awk '{if($3!="") print $3; else print $5}')
INITIAL_MAC=$(ip neighbor show | grep "$GATEWAY_IP" | awk '{print $5}')

echo "--- G1 CHAOS SENTINEL: ADAPTIVE MODE ACTIVE ---"

while true; do
    # 1. Verification Loops
    if [[ -z $(ifconfig 2>/dev/null | grep -E "wg0|tun0|p2p0") ]]; then
        ANOMALY="VPN_DROP"
    fi
    
    CURRENT_MAC=$(ip neighbor show | grep "$GATEWAY_IP" | awk '{print $5}')
    if [[ "$CURRENT_MAC" != "$INITIAL_MAC" && ! -z "$CURRENT_MAC" ]]; then
        ANOMALY="MAC_SPOOF"
    fi

    # 2. Automated Containment Sequence
    if [ ! -z "$ANOMALY" ]; then
        echo "[!] ANOMALY DETECTED: $ANOMALY. Initiating local containment."
        mkdir -p ~/.shadow_layer
        # Gracefully safe-stop local workspace parameters
        unset ANOMALY
        break
    fi
    sleep 0.5
done
