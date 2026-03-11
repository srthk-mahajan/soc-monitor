import time
from collections import defaultdict
from core.alert_manager import create_alert

attack_patterns = defaultdict(list)
CORRELATION_WINDOW = 60


def register_event(ip):

    now = time.time()

    attack_patterns[ip].append(now)

    attack_patterns[ip] = [
        t for t in attack_patterns[ip]
        if now - t < CORRELATION_WINDOW
    ]

    if len(attack_patterns[ip]) >= 3:

        create_alert(
            "MULTI_STAGE_INTRUSION",
            ip,
            "CRITICAL",
            "CORRELATION_ENGINE",
            "TA0001",
            "Multiple attack indicators observed"
        )

        attack_patterns[ip].clear()