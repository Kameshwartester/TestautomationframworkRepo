from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
driver.get("https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=laptop&crid=6MYET830HUWF&sprefix=laptop%2Caps%2C483")
elem = driver.find_element(By.CLASS_NAME,"puis-card-container")
#print(elem.text)
print(elem.get_attribute("outerHTML"))
time.sleep(5)
driver.close()