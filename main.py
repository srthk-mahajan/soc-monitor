import threading

from collectors.network_collector import start_network_collector
from collectors.auth_log_collector import start_auth_log_collector

from dashboard.soc_dashboard import dashboard

from intel.threat_intel import load_threat_intel
from intel.intel_updater import update_feed

from detection.sigma_engine import load_sigma_rules


def main():

    update_feed()          # download latest threat intel
    load_threat_intel()    # load into memory
    load_sigma_rules()

    net_thread = threading.Thread(
        target=start_network_collector,
        daemon=True
    )

    auth_thread = threading.Thread(
        target=start_auth_log_collector,
        daemon=True
    )

    net_thread.start()
    auth_thread.start()

    dashboard()


if __name__ == "__main__":
    main()