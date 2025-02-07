from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
for i in range(1,5):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=6MYET830HUWF&sprefix=laptop%2Caps%2C483&ref=nb_sb_noss_2")
    elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")
    print(f"{len(elems)} items found")
    #print(elem.text)
    #print(elem.get_attribute("outerHTML"))
    #print(elem.text)

    for elem in elems:
        print(elem.text)

    time.sleep(5)
driver.close()