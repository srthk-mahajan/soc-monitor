import json
import requests


ELASTIC_ENDPOINT = "http://localhost:9200/soc-alerts/_doc"


def export_event(event):

    try:

        requests.post(
            ELASTIC_ENDPOINT,
            headers={"Content-Type": "application/json"},
            data=json.dumps(event),
            timeout=1
        )

    except:
        pass