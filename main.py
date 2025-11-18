import yaml
from src.fetch_data import fetch_all_comics
from src.transformations import transform_comic
from src.into_bq import create_all_tables, insert_comics


with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

PROJECT_ID = config["project_id"]
DATASET_ID = config["dataset_id"]


def run_pipeline(start=1, end=10):
    create_all_tables()
    comics = fetch_all_comics(start, end)
    transformed = [transform_comic(c) for c in comics]
    insert_comics(transformed)

if __name__ == "__main__":
    run_pipeline()