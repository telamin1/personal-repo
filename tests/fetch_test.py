import unittest
from src.fetch_comics import fetch_comic, get_latest_comic_number

class TestFetchComics(unittest.TestCase):
    def test_fetch_latest_comic_number(self):
        latest_num = get_latest_comic_number()
        self.assertIsInstance(latest_num, int)
        self.assertGreater(latest_num, 0)

    def test_fetch_single_comic(self):
        comic = fetch_comic(1)
        self.assertIn("title", comic)
        self.assertIn("img", comic)
        self.assertEqual(comic["num"], 1)

if __name__ == "__main__":
    unittest.main()
