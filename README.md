# XKCD Data Project

## Overview
This project fetches comic data from the [XKCD API](https://xkcd.com/json.html), applies business logic (cost, views and reviews), and loads the data into Google BigQuery for analysis (modelling) and visualization.


### Business Rules
- *Cost*: Creators are paid €5 per letter in the comic title.
- *Views*: Random number between 0 and 10,000.
- *Customer Reviews*: Random number between 1.0 and 10.0.


## Features
- Fetch all XKCD comics or a specified range.
- Transformation of data with calculated metrics.
- Store data in BigQuery using a **Kimball-style dimensional model**:
  - `dimension_comic` (comic details)
  - `fact_comic_metrics` (views, cost, reviews)
  - `dimension_date` (date dimension)
