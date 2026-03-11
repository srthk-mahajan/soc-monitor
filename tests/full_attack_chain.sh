#!/bin/bash

echo "SOC Full Attack Chain Simulation"
echo "--------------------------------"

# Step 1: Recon
echo "[1] Recon - Port Scan"

nmap -sS -p 1-200 localhost

sleep 2

# Step 2: Enumeration
echo "[2] Service Enumeration"

for i in {1..10}
do
    nc -z localhost 22
    nc -z localhost 3306
done

sleep 2

# Step 3: Brute Force
echo "[3] SSH Brute Force"

for i in {1..10}
do
    ssh invaliduser@localhost
done

echo "Attack chain simulation complete"