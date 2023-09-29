import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:

    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    a_element = driver.find_element(By.ID, "column-a")
    b_element = driver.find_element(By.ID, "column-b")

    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(a_element, b_element)
    action_chains.perform()
    time.sleep(3)

    a_element = driver.find_element(By.ID, "column-a")
    b_element = driver.find_element(By.ID, "column-b")
    action_chains.drag_and_drop(b_element, a_element)
    action_chains.perform()
    time.sleep(10)

finally:
    driver.quit()
