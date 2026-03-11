from collections import defaultdict

attack_stats = defaultdict(lambda: {
    "count": 0,
    "types": set(),
    "mitre": set(),
    "severity": set()
})


def register_attack(ip, alert_type, mitre, severity):

    entry = attack_stats[ip]

    entry["count"] += 1
    entry["types"].add(alert_type)
    entry["mitre"].add(mitre)
    entry["severity"].add(severity)


def get_scoreboard():

    data = []

    for ip, info in attack_stats.items():

        data.append({
            "ip": ip,
            "count": info["count"],
            "types": ",".join(info["types"]),
            "mitre": ",".join(info["mitre"]),
            "severity": ",".join(info["severity"])
        })

    return sorted(data, key=lambda x: x["count"], reverse=True)