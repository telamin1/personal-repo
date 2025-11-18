import logging
import requests
from typing import Dict, List
from google.cloud import bigquery

import requests
import logging

XKCD_LATEST_URL = "https://xkcd.com/info.0.json"
XKCD_COMIC_URL_TEMPLATE = "https://xkcd.com/{comic_number}/info.0.json"

logger = logging.getLogger(__name__)

def get_latest_comic_number():
    response = requests.get(XKCD_LATEST_URL)
    response.raise_for_status()
    return response.json()["num"]

def fetch_comic(comic_number):
    url = XKCD_COMIC_URL_TEMPLATE.format(comic_number=comic_number)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_all_comics(start=1, end=None):
    if end is None:
        end = get_latest_comic_number()
    comics = []
    for num in range(start, end + 1):
        try:
            comics.append(fetch_comic(num))
        except Exception as e:
            logger.error(f"Error fetching comic #{num}: {e}")
    return comics

# Logger Setup
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Constants

PROJECT_ID = "comics-data-project"
DATASET_ID = "xkcd_dataset"
TABLE_ID = "comics_data"
XKCD_LATEST_URL = "https://xkcd.com/info.0.json"
XKCD_COMIC_URL_TEMPLATE = "https://xkcd.com/{comic_number}/info.0.json"

# BigQuery schema
SCHEMA = [
    bigquery.SchemaField("num", "INTEGER"),
    bigquery.SchemaField("title", "STRING"),
    bigquery.SchemaField("img", "STRING"),
    bigquery.SchemaField("alt", "STRING"),
    bigquery.SchemaField("year", "STRING"),
    bigquery.SchemaField("month", "STRING"),
    bigquery.SchemaField("day", "STRING"),
]

# BigQuery client
bq_client = bigquery.Client(project=PROJECT_ID)


# Helper Functions


def get_latest_comic_number() -> int:
    """Fetch the latest comic number from XKCD API."""
    logger.debug("Fetching latest comic number")
    response = requests.get(XKCD_LATEST_URL)
    response.raise_for_status()
    latest_num = response.json()["num"]
    logger.info(f"Latest comic number: {latest_num}")
    return latest_num


def fetch_comic(comic_number: int) -> Dict:
    """Fetch a specific comic by number."""
    url = XKCD_COMIC_URL_TEMPLATE.format(comic_number=comic_number)
    logger.debug(f"Fetching comic #{comic_number} from {url}")
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def insert_into_bigquery(data: Dict):
    """Insert comic data into BigQuery table."""
    rows_to_insert = [{
        "num": data["num"],
        "title": data["title"],
        "img": data["img"],
        "alt": data["alt"],
        "year": data["year"],
        "month": data["month"],
        "day": data["day"]
    }]
    errors = bq_client.insert_rows_json(f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}", rows_to_insert)
    if errors:
        logger.error(f"Failed to insert comic #{data['num']}: {errors}")
    else:
        logger.info(f"Inserted comic #{data['num']} - {data['title']}")


def create_table_if_not_exists():
    """Create BigQuery table if it does not exist."""
    table_ref = bq_client.dataset(DATASET_ID).table(TABLE_ID)
    try:
        bq_client.get_table(table_ref)
        logger.info("Table already exists")
    except Exception:
        logger.info("Creating BigQuery table")
        table = bigquery.Table(table_ref, schema=SCHEMA)
        bq_client.create_table(table)
        logger.info("Table created successfully")

# Main Pipeline

def run_xkcd_pipeline(start: int = 1, end: int = None):
    """Fetch XKCD comics and load into BigQuery."""
    try:
        logger.info("XKCD Pipeline: Started")
        create_table_if_not_exists()

        if end is None:
            end = get_latest_comic_number()

        for comic_number in range(start, end + 1):
            try:
                comic_data = fetch_comic(comic_number)
                insert_into_bigquery(comic_data)
            except Exception as e:
                logger.error(f"Error processing comic #{comic_number}: {e}")

        logger.info("XKCD Pipeline: Successfully Finished")

    except Exception as e:
        logger.error(f"XKCD Pipeline: Failed due to {e}")


if __name__ == "__main__":
    run_xkcd_pipeline(start=1, end=None)

    