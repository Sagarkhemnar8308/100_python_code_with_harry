from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import os

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Define the search URL
url1 = 'https://www.linkedin.com/jobs/search?keywords=Marketing%20Data%20Analyst&location=Berlin%2C%20Berlin%2C%20Germany&geoId=106967730&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

# Set up the ChromeDriver service
service = Service(executable_path=r"C:\\Users\\sagar\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get(url1)
driver.implicitly_wait(50)

elements = driver.find_elements(By.CLASS_NAME, 'filter-values-container__filter-value')
print(f"Number of elements found: {len(elements)}")

for element in elements:
    print(f"Element text is: {element.text}")

driver.quit()

driver.quit()
