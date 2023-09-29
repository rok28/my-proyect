import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:

    driver.get("https://the-internet.herokuapp.com/tables")
    elements = driver.find_elements(By.CSS_SELECTOR, "#table1 > tbody > tr > td:nth-child(4)")
    suma = 0

    for element in elements:
        suma = suma + int(element.text.split('$')[1].split('.')[0])

    time.sleep(3)
    #print(suma)
    assert suma == 251
finally:
    driver.quit()
