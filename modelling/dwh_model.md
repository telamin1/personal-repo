# Data Warehouse Model for XKCD Pipeline

This document describes the dimensional model used for storing XKCD comic data in BigQuery. The model follows Kimball's star schema approach for easy analysis and visualisation.

## Business Requirements
- Track comic details (title, image, alt text, date).
- Calculate and store metrics:
  - Cost (based on title length).
  - Views (randomised for simulation).
  - Customer review score.
- Enable analysis by date and comic attributes.

  ## Dimensional Model
The model consists of:
- dime_comic: Stores static comic details.
- dim_date: Stores date attributes for time-based analysis.
- fact_comic_mtrics: Stores calculated metrics linked to comics and dates.

### Dim_Comic
- comic_id (PK)
- title
- img_url
- alt_text
- year, month, day

### Dim_Date
- date_id (PK)
- date
- year, month, day

### Fact_ComicMetrics
- comic_id (FK → dim_comic)
- date_id (FK → dim_date)
- views
- cost
- review_score
  
## Why Star Schema?
- Simplifies queries for BI tools.
- Supports slicing and dicing by comic attributes and time.
- Scales well for analytical workloads.
