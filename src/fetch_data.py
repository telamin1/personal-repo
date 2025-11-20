import requests
import logging

XKCD_LATEST_URL = "https://xkcd.com/info.0.json"
XKCD_COMIC_URL_TEMPLATE = "https://xkcd.com/{comic_number}/info.0.json"

logger = logging.getLogger(__name__)

def get_latest_comic_number():
    response = requests.get(XKCD_LATEST_URL)
    response.raise_for_status()
    return response.json()["num"]

def fetch_comic(comic_number):
    url = XKCD_COMIC_URL_TEMPLATE.format(comic_number=comic_number)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_all_comics(start=1, end=None):
    if end is None:
        end = get_latest_comic_number()
    comics = []
    for num in range(start, end + 1):
        try:
            comics.append(fetch_comic(num))
        except Exception as e:
            logger.error(f"Error fetching comic #{num}: {e}")
    return comics

