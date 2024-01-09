import json

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
BASE_URL = "https://realtylink.org/"
FIRST_PAGE_URL = "https://realtylink.org/en/properties~for-rent?uc=2"

APARTMENTS_DATA = []


def parse_main_page(url, max_pages=3):
    page_count = 0
    while page_count < max_pages:
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            apartments = soup.find_all("div", class_="property-thumbnail-item thumbnailItem col-12 col-sm-6 col-md-4 col-lg-3")
            for apartment in apartments:
                link = BASE_URL + str(apartment.find("a", class_="property-thumbnail-summary-link")).split()[2][7:-2]
                parse_details_page(link)
                if len(APARTMENTS_DATA) == 60:
                    break

            wait = WebDriverWait(driver, 10)
            next_page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.next a")))
            next_page_button.click()

            page_count += 1
        else:
            print(f"Request error: {response.status_code}")


def parse_details_page(url):
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        title = extract_title(soup)
        region, address = extract_location(soup)
        description = extract_description(soup)
        images = extract_images(soup)
        price = extract_price(soup)
        rooms_quantity = extract_rooms_quantity(soup)
        floor_area = extract_floor_area(soup)

        apartment_data = {
            "link": url,
            "title": title,
            "region": region,
            "address": address,
            "description": description,
            "images": images,
            "price": price,
            "rooms_quantity": rooms_quantity,
            "floor_area": floor_area
        }

        APARTMENTS_DATA.append(apartment_data)

    else:
        print(f"Request error: {response.status_code}")


def extract_title(soup):
    title_tag = soup.find("span", {"data-id": "PageTitle"})
    return title_tag.text.strip() if title_tag else None


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