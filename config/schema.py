from google.cloud import bigquery

DIMENSION_COMIC_SCHEMA = [
    bigquery.SchemaField("comic_id", "INTEGER"),
    bigquery.SchemaField("title", "STRING"),
    bigquery.SchemaField("img_url", "STRING"),
    bigquery.SchemaField("alt_text", "STRING"),
    bigquery.SchemaField("year", "STRING"),
    bigquery.SchemaField("month", "STRING"),
    bigquery.SchemaField("day", "STRING"),
]

FACT_COMIC_METRICS_SCHEMA = [
    bigquery.SchemaField("comic_id", "INTEGER"),
    bigquery.SchemaField("date_id", "INTEGER"),
    bigquery.SchemaField("views", "FLOAT"),
    bigquery.SchemaField("cost", "FLOAT"),
    bigquery.SchemaField("review_score", "FLOAT"),
]

DIMENSION_COMIC_TABLE = "dimensions_comic"
FACT_COMIC_METRICS_TABLE = "fact_comic_metrics"
DATASET_ID = "xkcd_dummy_dataset"