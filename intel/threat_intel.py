MALICIOUS_IPS = set()


def load_threat_intel():

    global MALICIOUS_IPS

    files = [
        "threat_intel/emerging_threats.txt",
        "threat_intel/custom_blocklist.txt"
    ]

    MALICIOUS_IPS.clear()

    for file in files:

        try:

            with open(file) as f:

                for line in f:

                    ip = line.strip()

                    if ip:
                        MALICIOUS_IPS.add(ip)

        except:
            pass

    print(f"[+] Threat intel loaded: {len(MALICIOUS_IPS)} IPs")


def is_malicious(ip):

    return ip in MALICIOUS_IPS