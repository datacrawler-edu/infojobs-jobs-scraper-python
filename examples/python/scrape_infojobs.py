"""Run the hosted InfoJobs Actor and print Dataset items."""

from __future__ import annotations

import json
import os

from apify_client import ApifyClient


ACTOR_ID = "datascraperes/infojobs-jobs-scraper"


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    actor_input = {
        "keyword": "python",
        "location": "Madrid",
        "remote": "any",
        "contractType": "any",
        "workday": "any",
        "publishedWithinDays": "any",
        "sortBy": "relevance",
        "maxItems": 5,
        "includeDetails": False,
    }

    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=actor_input)
    dataset_id = run["defaultDatasetId"]
    items = list(client.dataset(dataset_id).iterate_items())
    print(json.dumps(items, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

