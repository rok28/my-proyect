import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from pageobjects.loginpage import LoginlPage

driver: WebDriver = webdriver.Chrome()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    login_page = LoginlPage(driver)

    login_page.tbx__username().send_keys("Rokzero")
    login_page.tbx__password().send_keys("hjhuqjeie")
    login_page.btn__login.click()

finally:
    time.sleep(3)
    driver.quit()
