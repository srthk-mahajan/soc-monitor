import os
import time

from core.alert_manager import get_recent_alerts
from dashboard.attack_timeline import get_timeline
from dashboard.attack_scoreboard import get_scoreboard


def dashboard():

    while True:

        alerts = get_recent_alerts()
        timeline = get_timeline()
        scoreboard = get_scoreboard()

        os.system("clear")

        print("""
===================================================
              SOC SECURITY OPERATIONS
===================================================
""")

        # --------------------------
        # Recent Alerts
        # --------------------------

        print("Recent Alerts")
        print("-------------------------------------------")

        if alerts:

            for a in alerts[:10]:

                print(
                    f"[{a['severity']}] "
                    f"{a['type']} | "
                    f"{a['source_ip']} | "
                    f"{a['mitre']}"
                )

        else:
            print("No alerts")

        # --------------------------
        # Top Attackers
        # --------------------------

        print("\nTop Attackers")
        print("-------------------------------------------")

        if scoreboard:

            for row in scoreboard[:5]:

                print(
                    f"{row['ip']} | "
                    f"alerts:{row['count']} | "
                    f"type:{row['types']} | "
                    f"MITRE:{row['mitre']}"
                )

        else:
            print("None")

        # --------------------------
        # Attack Timeline
        # --------------------------

        print("\nAttack Timeline")
        print("-------------------------------------------")

        if timeline:

            for t, ip in timeline[:10]:

                print(f"{t}  {ip}")

        else:
            print("No activity")

        time.sleep(2)