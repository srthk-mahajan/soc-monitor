# 🛡️ SOC Threat Monitoring Platform

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux-green.svg)
![Category](https://img.shields.io/badge/Category-SOC%20Monitoring-red.svg)

A lightweight **Security Operations Center (SOC) style threat monitoring platform** built in Python that performs real-time network telemetry monitoring, authentication log analysis, threat intelligence correlation, and automated attack detection.

This project simulates how real **Security Operations Centers detect and respond to attacks**.

---

# 📌 Overview

Modern SOC environments rely on multiple telemetry sources to identify malicious behavior.

This project monitors:

- Network packets
- Authentication logs
- Threat intelligence feeds

It applies **rule-based detection, Sigma rules, and event correlation** to identify suspicious activity and generate alerts mapped to **MITRE ATT&CK techniques**.

The system includes a **real-time SOC dashboard** and **automated attacker blocking**.

---

# 🚀 Features

### 📡 Network Telemetry Monitoring
- Live packet capture using **Scapy**
- TCP traffic inspection
- Detection of suspicious scanning and traffic patterns

### 🔐 Authentication Monitoring
- SSH authentication log monitoring via **journalctl**
- Detection of brute-force login attempts

### 🌐 Threat Intelligence Integration
- Automatic ingestion of **Emerging Threats IP feed**
- Custom blocklist support
- Detection of known malicious infrastructure

### 🧠 Detection Engine
Detection rules implemented:

- Port scan detection
- Sensitive service enumeration
- Traffic burst detection
- SSH brute-force detection
- Threat intelligence matches

### 🧩 Sigma Rule Support
Supports **Sigma detection rules** for log analysis.

### 🎯 MITRE ATT&CK Mapping

| Technique | Description |
|----------|-------------|
| T1046 | Network Service Scanning |
| T1110 | Brute Force |
| T1589 | Victim Identity Information |

### 🔗 Event Correlation
Detects multi-stage attacks by correlating suspicious activities.

### 🚫 Automated Response
Automatically blocks attacker IPs using firewall rules.

### 📊 SOC Dashboard
Displays:

- Recent alerts
- Attack timeline
- Top attackers
- Alert severity

---

# 🏗️ Architecture

```text
Network Traffic / Logs
          │
          ▼
Collectors
(Network + Auth Logs)
          │
          ▼
Detection Engine
(Rule-Based + Sigma)
          │
          ▼
Threat Intelligence Correlation
          │
          ▼
Alert Manager
          │
          ▼
SOC Dashboard
```

---

# 📂 Project Structure

```text
soc-threat-monitor/
│
├── collectors/
│   ├── network_collector.py
│   └── auth_log_collector.py
│
├── detection/
│   ├── network_rules.py
│   ├── auth_rules.py
│   ├── sigma_engine.py
│   └── correlation_engine.py
│
├── dashboard/
│   ├── soc_dashboard.py
│   ├── attack_timeline.py
│   └── attack_scoreboard.py
│
├── intel/
│   ├── threat_intel.py
│   └── intel_updater.py
│
├── response/
│   └── firewall_blocker.py
│
├── export/
│   └── elastic_exporter.py
│
├── config/
│   └── detection_rules.yaml
│
├── sigma_rules/
│   └── ssh_bruteforce.yml
│
├── tests/
│   ├── network_test.sh
│   ├── auth_test.sh
│   └── spoof_attack.py
│
├── threat_intel/
│   ├── emerging_threats.txt
│   └── custom_blocklist.txt
│
├── main.py
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOURUSERNAME/soc-threat-monitor.git
cd soc-threat-monitor
```

Create a virtual environment:

```bash
python3 -m venv socenv
source socenv/bin/activate
```

Install dependencies:

```bash
pip install scapy pyyaml requests
```

Run the SOC platform:

```bash
sudo python main.py
```

Root privileges are required for packet capture.

---

# 🧪 Attack Simulation

### Network Attack Simulation

```bash
bash tests/network_test.sh
```

Simulates:

- Port scanning
- Sensitive service probing
- Traffic bursts

---

### SSH Brute Force Simulation

```bash
bash tests/auth_test.sh
```

Simulates repeated SSH login attempts.

---

### Spoofed Attacker Simulation

```bash
sudo python tests/spoof_attack.py
```

Simulates multi-stage attacks using spoofed attacker IPs.

---

# 📋 Example Alerts

```text
[HIGH] PORT_SCAN_DETECTED | 185.220.101.1 | T1046
[MEDIUM] SERVICE_ENUMERATION | 185.220.101.1 | T1046
[CRITICAL] THREAT_INTEL_MATCH | 185.220.101.1 | T1589
```

---

# 🌍 Threat Intelligence Feed

The system automatically downloads threat intelligence from:

```
https://rules.emergingthreats.net/blockrules/compromised-ips.txt
```

Custom malicious IPs can be added to:

```
threat_intel/custom_blocklist.txt
```

---

# 🔮 Future Improvements

Potential enhancements:

- Web-based SOC dashboard
- Machine learning anomaly detection
- PCAP replay attack simulation
- Threat intelligence enrichment APIs
- SIEM integrations (Elastic / Splunk)

---

# 📚 Educational Purpose

This project was built to explore **SOC detection workflows**, including:

- telemetry collection
- attack detection
- event correlation
- automated response

It demonstrates core concepts used in modern **Security Operations Centers**.
