import unittest
from src.transform import calculate_metrics, transform_comic

class TestTransform(unittest.TestCase):
    def test_calculate_metrics(self):
        metrics = calculate_metrics("TestTitle")
        self.assertEqual(metrics["cost"], len("TestTitle") * 5)
        self.assertGreaterEqual(metrics["views"], 0)
        self.assertLessEqual(metrics["views"], 10000)
        self.assertGreaterEqual(metrics["review_score"], 1.0)
        self.assertLessEqual(metrics["review_score"], 10.0)

    def test_transform_comic(self):
        comic_data = {
            "num": 1,
            "title": "TestTitle",
            "img": "http://example.com/img.png",
            "alt": "Alt text",
            "year": "2025",
            "month": "11",
            "day": "17"
        }
        transformed = transform_comic(comic_data)
        self.assertIn("cost", transformed)
        self.assertIn("views", transformed)
        self.assertIn("review_score", transformed)

if __name__ == "__main__":
    unittest.main()
