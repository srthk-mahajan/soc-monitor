#!/bin/bash

echo "SOC Network Attack Simulation"
echo "-----------------------------"

TARGET=localhost

# ----------------------------
# Port Scan
# ----------------------------

echo "[1] Port Scan Test"

nmap -sS -p 1-1000 -T4 $TARGET

sleep 2

# ----------------------------
# Sensitive Port Enumeration
# ----------------------------

echo "[2] Sensitive Port Enumeration"

for i in {1..12}
do
    nc -z $TARGET 22
    nc -z $TARGET 3306
    nc -z $TARGET 3389
done

sleep 2

# ----------------------------
# Traffic Burst
# ----------------------------

echo "[3] Traffic Burst Test"

for i in {1..250}
do
    nc -z $TARGET $((RANDOM%65535)) &
done

wait

echo "Network simulation complete."