import json

import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
BASE_URL = "https://realtylink.org/"
FIRST_PAGE_URL = "https://realtylink.org/en/properties~for-rent?uc=2"

APARTMENTS_DATA = []


def main():
    driver = webdriver.Chrome()
    driver.get("https://realtylink.org/en/properties~for-rent?uc=2")
    try:
        parse_main_page(FIRST_PAGE_URL, max_pages=3)
    finally:
        driver.quit()

    with open("apartments_data.json", "w", encoding="utf-8") as json_file:
        json.dump(APARTMENTS_DATA, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()