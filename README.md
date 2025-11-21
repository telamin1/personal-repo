# XKCD Data Project

## Overview
This project fetches comic data from the [XKCD API](https://xkcd.com/json.html), applies business logic (cost, views and reviews), and loads the data into Google BigQuery for analysis (modelling) and visualisation.


### Business Rules
- *Cost*: Creators are paid €5 per letter in the comic title.
- *Views*: Random number between 0 and 10,000.
- *Customer Reviews*: Random number between 1.0 and 10.0.


## Features
- Fetch all XKCD comics or a specified range.
- Transformation of data with calculated metrics.
- Store data in BigQuery using a **Kimball-style dimensional model**:
  - `dim_comic` (comic details)
  - `fact_comic_metrics` (views, cost, reviews)
  - `dime_date` (date dimension)

## Set up instructions
- Clone the Repository
```bash
git clone https://github.com/telamin1/xkcd-data-pipeline.git
cd xkcd-data-pipeline
- pip install -r requirements.txt
- run the pipeline python src/main.py
