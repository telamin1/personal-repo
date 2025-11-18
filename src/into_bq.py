from google.cloud import bigquery
import logging
from config.schema import DIM_COMIC_SCHEMA, FACT_COMIC_METRICS_SCHEMA

logger = logging.getLogger(__name__)

def create_table_if_not_exists(project_id, dataset_id, table_name, schema):
    client = bigquery.Client(project=project_id)
    table_ref = client.dataset(dataset_id).table(table_name)
    try:
        client.get_table(table_ref)
        logger.info(f"Table {table_name} exists.")
    except Exception:
        table = bigquery.Table(table_ref, schema=schema)
        client.create_table(table)
        logger.info(f"Created table {table_name}.")

def create_all_tables(project_id, dataset_id):
    create_table_if_not_exists(project_id, dataset_id, "dim_comic", DIM_COMIC_SCHEMA)
    create_table_if_not_exists(project_id, dataset_id, "fact_comic_metrics", FACT_COMIC_METRICS_SCHEMA)

def insert_comics(comics, project_id, dataset_id):
    client = bigquery.Client(project=project_id)
    dim_rows = [{
        "comic_id": c["comic_id"], "title": c["title"], "img_url": c["img_url"],
        "alt_text": c["alt_text"], "year": c["year"], "month": c["month"], "day": c["day"]
    } for c in comics]

    fact_rows = [{
        "comic_id": c["comic_id"], "date_id": c["comic_id"],
        "views": c["views"], "cost": c["cost"], "review_score": c["review_score"]
    } for c in comics]

    client.insert_rows_json(f"{project_id}.{dataset_id}.dim_comic", dim_rows)
    client.insert_rows_json(f"{project_id}.{dataset_id}.fact_comic_metrics", fact_rows)