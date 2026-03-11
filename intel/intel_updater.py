import requests
import os

FEED_URL = "https://rules.emergingthreats.net/blockrules/compromised-ips.txt"

OUTPUT_FILE = "threat_intel/emerging_threats.txt"


def update_feed():

    print("[+] Updating threat intelligence feed...")

    try:

        r = requests.get(FEED_URL, timeout=10)

        lines = r.text.splitlines()

        ips = []

        for line in lines:

            line = line.strip()

            if line and not line.startswith("#"):

                ips.append(line)

        os.makedirs("threat_intel", exist_ok=True)

        with open(OUTPUT_FILE, "w") as f:

            for ip in ips:
                f.write(ip + "\n")

        print(f"[+] Loaded {len(ips)} emerging threat IPs")

    except Exception as e:

        print("[!] Threat intel update failed:", e)