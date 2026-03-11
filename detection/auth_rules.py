import time
import yaml
from collections import defaultdict
from core.alert_manager import create_alert

rules = yaml.safe_load(open("config/detection_rules.yaml"))

ssh_tracker = defaultdict(list)


def process_ssh_failure(ip):

    now = time.time()

    ssh_tracker[ip].append(now)

    ssh_tracker[ip] = [
        t for t in ssh_tracker[ip]
        if now - t < rules["ssh_bruteforce"]["window_seconds"]
    ]

    failures = len(ssh_tracker[ip])
    thresholds = rules["ssh_bruteforce"]["thresholds"]

    severity = None

    if failures >= thresholds["CRITICAL"]:
        severity = "CRITICAL"
    elif failures >= thresholds["HIGH"]:
        severity = "HIGH"
    elif failures >= thresholds["MEDIUM"]:
        severity = "MEDIUM"

    if severity:

        create_alert(
            "SSH_BRUTE_FORCE",
            ip,
            severity,
            "AUTH_LOG",
            rules["ssh_bruteforce"]["mitre"],
            f"{failures} failed login attempts"
        )