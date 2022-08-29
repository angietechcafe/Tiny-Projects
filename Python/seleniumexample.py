# use selenium to scrape an image. 
from selenium import webdriver
#use an explicit wait since the code can load faster than the browser.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# use HTTP requests to get info
import requests 
import magic
import time

# Get GitHub Url and store it in a variable
GitHub_url = input("Please enter your GitHub url here: https://github.com/ ")

# Fetch the request?

# find_element_by_xpath
# driver.find_element_by_xpath(//input[@AttributeName='value aka AttributeValue'])

# wait 20 seconds using explicit wait & use xpath to click on the image
driver = webdriver.Firefox()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="image"][@src="/images/#"]'))).click()
finally:
    driver.quit()
