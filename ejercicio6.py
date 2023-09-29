import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://the-internet.herokuapp.com/checkboxes"

def checkboxes(check1, check2):

    driver = webdriver.Chrome()
    try:
        driver.get(URL)
        checks = driver.find_elements(By.CSS_SELECTOR,"#checkboxes > input[type=checkbox]")
        chk_check1= checks[0]
        chk_check2= checks[1]

        chk_check1_checked =chk_check1.get_property("checked")
        chk_check2_checked =chk_check2.get_property("checked")

        if (chk_check1_checked and not check1) or (not chk_check1_checked and check1):
            chk_check1.click()
        if (chk_check2_checked and not check2) or (not chk_check2_checked and check2):
            chk_check2.click()


    finally:
        time.sleep(3)
        driver.close()


checkboxes(True, True)
checkboxes(True, False)
checkboxes(False, False)
checkboxes(False, True)
