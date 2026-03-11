import os
import yaml

from core.alert_manager import create_alert

SIGMA_RULES = []


def load_sigma_rules():

    rule_dir = "sigma_rules"

    for file in os.listdir(rule_dir):

        if file.endswith(".yml") or file.endswith(".yaml"):

            path = os.path.join(rule_dir, file)

            with open(path) as f:
                rule = yaml.safe_load(f)

            SIGMA_RULES.append(rule)


def evaluate_log(line, src_ip):

    for rule in SIGMA_RULES:

        detection = rule.get("detection", {})

        selection = detection.get("selection", {})

        for key, value in selection.items():

            if "contains" in key:

                for word in value:

                    if word in line:

                        create_alert(
                            alert_type=rule["title"].upper().replace(" ", "_"),
                            source_ip=src_ip,
                            severity=rule.get("level", "MEDIUM").upper(),
                            module="SIGMA_ENGINE",
                            mitre=",".join(rule.get("tags", [])),
                            details="Sigma rule triggered"
                        )