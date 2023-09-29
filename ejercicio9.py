import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:

    driver.get("https://the-internet.herokuapp.com/windows")
    driver.find_element(By.CSS_SELECTOR, "#content > div > a").click()


    time.sleep(3)

    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
    driver.close()
    
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[0])

    time.sleep(3)
    driver.close()

finally:
    driver.quit()
