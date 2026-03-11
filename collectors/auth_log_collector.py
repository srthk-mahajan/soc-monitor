import subprocess
import re

from detection.auth_rules import process_ssh_failure
from detection.sigma_engine import evaluate_log


def extract_ip(line):

    match = re.search(r'from ([0-9a-fA-F:.]+)', line)

    if match:
        return match.group(1)

    return None


def start_auth_log_collector():

    process = subprocess.Popen(
        ["journalctl","-f","-n","0","-u","ssh"],
        stdout=subprocess.PIPE,
        text=True
    )

    for line in process.stdout:

        ip = extract_ip(line)

        if ip:

            evaluate_log(line, ip)

            if "Failed password" in line:

                process_ssh_failure(ip)