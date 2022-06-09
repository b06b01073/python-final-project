from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

url = "https://www.iucnredlist.org/species/153538/4516675"

# download chromedrive: https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome("./chromedriver")

# crawl the page by selenium 
driver.get(url)

# sleep for 3 secs to make sure the page is loaded completely
time.sleep(1)

html = driver.page_source

# pass the crawled page to beautifulsoup
soup = BeautifulSoup(html, "html.parser")

# select the <div> with id "threats-details"
result = soup.find("div", {"id": "threats-details"})

# write the result to ./result.txt
with open("result.txt", "w") as f:
    f.write(result.prettify())




