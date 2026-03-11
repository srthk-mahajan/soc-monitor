import os
import json
from datetime import datetime
from collections import deque

from dashboard.attack_timeline import add_event
from dashboard.attack_scoreboard import register_attack
from export.elastic_exporter import export_event

LOG_FILE = "logs/alerts.log"

recent_alerts = deque(maxlen=20)

COLORS = {
    "CRITICAL": "\033[95m",
    "HIGH": "\033[91m",
    "MEDIUM": "\033[93m",
    "LOW": "\033[92m"
}

RESET = "\033[0m"


def create_alert(alert_type, source_ip, severity, module, mitre, details=""):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    event = {
        "timestamp": timestamp,
        "type": alert_type,
        "source_ip": source_ip,
        "severity": severity,
        "module": module,
        "mitre": mitre,
        "details": details
    }

    # store for dashboard
    recent_alerts.appendleft(event)

    # update attack timeline
    add_event(source_ip)

    # update attack scoreboard
    register_attack(source_ip, alert_type, mitre, severity)

    color = COLORS.get(severity, "")

    print(
        color +
        f"[{timestamp}] {alert_type} | {source_ip} | {severity} | {mitre}" +
        RESET
    )

    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

    # export to SIEM
    export_event(event)


def get_recent_alerts():
    return list(recent_alerts)