import unittest
from unittest.mock import patch
from src.load_bigquery import insert_comics

class TestLoadBigQuery(unittest.TestCase):
    @patch("src.load_bigquery.bigquery.Client")
    def test_insert_comics(self, mock_client):
        comics = [{
            "comic_id": 1,
            "title": "TestTitle",
            "img_url": "http://example.com/img.png",
            "alt_text": "Alt text",
            "year": "2025",
            "month": "11",
            "day": "17",
            "cost": 50,
            "views": 5000,
            "review_score": 8.5
        }]
        insert_comics(comics, "test-project", "test-dataset")
        self.assertTrue(mock_client.called)

if __name__ == "__main__":
    unittest.main()
