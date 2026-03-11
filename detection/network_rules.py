import time
import yaml
from collections import defaultdict

from core.alert_manager import create_alert
from intel.threat_intel import is_malicious
from response.firewall_blocker import block_ip
from dashboard.attack_scoreboard import attack_stats
rules = yaml.safe_load(open("config/detection_rules.yaml"))

port_tracker = defaultdict(list)
rate_tracker = defaultdict(list)
sensitive_tracker = defaultdict(int)


def process_packet(src_ip, dst_port, flags):

    now = time.time()

    # ----------------------------
    # Threat Intel Detection
    # ----------------------------

    if is_malicious(src_ip):

        create_alert(
            "THREAT_INTEL_MATCH",
            src_ip,
            "CRITICAL",
            "THREAT_INTEL",
            "T1589",
            "IP matched internal threat intelligence feed"
        )
        if src_ip in attack_stats:

            if attack_stats[src_ip]["count"] > 50:

                block_ip(src_ip)
        

    # ----------------------------
    # Port Scan Detection
    # ----------------------------

    port_tracker[src_ip].append((dst_port, now))

    port_tracker[src_ip] = [
        (p, t) for p, t in port_tracker[src_ip]
        if now - t < rules["port_scan"]["window_seconds"]
    ]

    ports = {p for p, _ in port_tracker[src_ip]}

    if len(ports) >= rules["port_scan"]["threshold"]:

        create_alert(
            "PORT_SCAN_DETECTED",
            src_ip,
            rules["port_scan"]["severity"],
            "NETWORK",
            rules["port_scan"]["mitre"],
            f"{len(ports)} ports scanned"
        )

        port_tracker[src_ip].clear()

    # ----------------------------
    # Sensitive Port Enumeration
    # ----------------------------

    if dst_port in rules["sensitive_service_probe"]["ports"]:

        sensitive_tracker[src_ip] += 1

        if sensitive_tracker[src_ip] >= rules["sensitive_service_probe"]["threshold"]:

            create_alert(
                "SERVICE_ENUMERATION",
                src_ip,
                rules["sensitive_service_probe"]["severity"],
                "NETWORK",
                rules["sensitive_service_probe"]["mitre"],
                "Multiple sensitive service probes"
            )

            sensitive_tracker[src_ip] = 0

    # ----------------------------
    # Traffic Burst Detection
    # ----------------------------

    rate_tracker[src_ip].append(now)

    rate_tracker[src_ip] = [
        t for t in rate_tracker[src_ip]
        if now - t < 5
    ]

    if len(rate_tracker[src_ip]) >= rules["traffic_burst"]["threshold"]:

        create_alert(
            "TRAFFIC_ANOMALY",
            src_ip,
            rules["traffic_burst"]["severity"],
            "NETWORK",
            rules["traffic_burst"]["mitre"],
            "Suspicious traffic burst"
        )

        rate_tracker[src_ip].clear()