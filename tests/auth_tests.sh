#!/bin/bash

echo "SOC Authentication Attack Simulation"
echo "-------------------------------------"

TARGET=localhost

for i in {1..12}
do
    echo "Attempt $i"

    ssh -o ConnectTimeout=3 \
        -o PreferredAuthentications=password \
        -o PubkeyAuthentication=no \
        -o StrictHostKeyChecking=no \
        invaliduser@$TARGET

done

echo "Authentication test complete."