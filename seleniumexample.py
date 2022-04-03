# use selenium to scrape an image. 
from selenium import webdriver
#use an explicit wait since the code can load faster than the browser.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# use HTTP requests to get info
import requests 
import magic
import time
# find_element_by_xpath
# driver.find_element_by_xpath('//paste xpathfrom the website in here /input')

# wait 10 seconds using explicit wait
driver = webdriver.Firefox()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "#"))
    )
finally:
    driver.quit()
