import random

def calculate_metrics(title):
    cost = len(title) * 5
    views = random.random() * 10000
    review_score = random.uniform(1.0, 10.0)
    return {"cost": cost, "views": views, "review_score": review_score}

def transform_comic(comic_data):
    metrics = calculate_metrics(comic_data["title"])
    return {
        "comic_id": comic_data["num"],
        "title": comic_data["title"],
        "img_url": comic_data["img"],
        "alt_text": comic_data["alt"],
        "year": comic_data["year"],
        "month": comic_data["month"],
        "day": comic_data["day"],
        **metrics
    }