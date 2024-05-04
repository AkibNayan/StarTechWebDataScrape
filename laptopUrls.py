from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=option)

for page in range(1, 10):
    url = f"https://www.startech.com.bd/laptop-notebook/laptop?limit=90&page={page}"
    driver.get(url)
    time.sleep(2)
    urls = driver.find_elements('xpath', '//div[@class="p-item-img"]//a')

    with open('laptopUrls.txt', 'a') as file:
        for url in urls:
            file.write(url.get_attribute('href') + '\n')

