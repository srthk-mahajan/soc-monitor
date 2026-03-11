import subprocess

BLOCKED = set()

def block_ip(ip):

    print(f"[DEBUG] Attempting to block {ip}")

    if ip.startswith("127.") or ip.startswith("192.168"):
        print("[DEBUG] Skipping local/private IP")
        return

    if ip in BLOCKED:
        print("[DEBUG] Already blocked")
        return

    try:

        subprocess.run(
            ["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
            check=True
        )

        BLOCKED.add(ip)

        print(f"[AUTO RESPONSE] Blocked IP {ip}")

    except Exception as e:

        print("[BLOCK ERROR]", e)