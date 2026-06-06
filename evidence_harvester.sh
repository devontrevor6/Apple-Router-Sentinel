#!/bin/bash
# SNTL EVIDENCE SCAN - Forensic Scraper Core

VAULT="$HOME/Apple-Router-Sentinel/artifacts"
DEST="$HOME/Apple-Router-Sentinel/evidence_locker"

mkdir -p "$DEST"

echo "--- SNTL EVIDENCE SCAN: STARTING ---"

# 1. Audit files for embedded hidden media extensions
echo "[!] HUNTING FOR MEDIA & CONTACTS..."
grep -i "JFIF\|PNG\|mp4" "$VAULT"/* > "$DEST/media_sources.txt" 2>/dev/null

# 2. Extract lines containing potential authentication blocks
echo "[!] EXTRACTING PASSWORDS & LOGINS..."
grep -rEi "pass|pwd|login|user|creds" "$VAULT"/ > "$DEST/found_credentials.txt" 2>/dev/null

# 3. Pluck clean email strings using strict POSIX character classes
echo "[!] MAPPING MALICIOUS CONTACTS..."
grep -rEo "[[:alnum:]+\._-]+@[[:alnum:]+\._-]+\.[[:alpha:]]{2,4}" "$VAULT"/ > "$DEST/extracted_emails.txt" 2>/dev/null

echo "--- SCAN COMPLETE: CHECK $DEST ---"
