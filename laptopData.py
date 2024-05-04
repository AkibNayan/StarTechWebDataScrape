from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import pandas as pd

option = webdriver.ChromeOptions()
#option.add_argument("--headless")
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=option)
data = []
count = 1
with open('laptopUrls.txt', 'r') as file:
    for url in file:
        driver.get(url.strip())
        #time.sleep(1)
        title = driver.find_element('xpath', '//h1[@class="product-name"]').text
        #print(title)
        sys.stdout.reconfigure(encoding='utf-8')
        price = driver.find_element(
            'xpath', '//td[@class="product-info-data product-price"]').text
        #print(price)
        status = driver.find_element(
            'xpath', '//td[@class="product-info-data product-status"]').text
        #print(status)
        brand = driver.find_element(
            'xpath', '//td[@class="product-info-data product-brand"]').text
        #print(brand)
        shortDesc = driver.find_elements(
            'xpath', '//div[@class="short-description"]//li')
        desc = []
        #print(len(shortDesc))
        count = 1
        for des in shortDesc:
            if count == len(shortDesc):
                break
            desc.append(des.text)
            count += 1
        #print(desc)
        longDescription = driver.find_elements(
            'xpath', '//td[@class="name"]')
        for index, category in enumerate(longDescription, start=1):
            if category.text == "Processor Brand":
                processorBrand = driver.find_element(
                    'xpath', f'(//td[@class="value"])[{index}]').text
            elif category.text == "Processor Model":
                processorModel = driver.find_element(
                    'xpath', f'(//td[@class="value"])[{index}]').text
            elif category.text == "Display Size":
                displaySize = driver.find_element(
                    'xpath', f'(//td[@class="value"])[{index}]').text
            elif category.text == "RAM":
                ram = driver.find_element(
                    'xpath', f'(//td[@class="value"])[{index}]').text
            elif category.text == "RAM Type":
                ramType = driver.find_element(
                    'xpath', f'(//td[@class="value"])[{index}]').text
            elif category.text == "Storage Capacity":
                storageCapacity = driver.find_element(
                    'xpath', f'(//td[@class="value"])[{index}]').text
        dict_ = {
            "title": title,
            "price" : price,
            "status" : status,
            "brand" : brand,
            "shortDescription" : desc,
            "processorBrand": processorBrand,
            "processorModel" : processorModel,
            "displaySize" : displaySize,
            "ram" : ram,
            "ramType" : ramType,
            "storageCapacity" : storageCapacity
        }
        data.append(dict_)
        
df = pd.DataFrame(data)
df.to_csv("StarTechLaptopSeleniumData.csv", index=False)