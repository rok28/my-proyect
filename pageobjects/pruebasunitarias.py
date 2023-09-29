import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAlert(unittest.TestCase):

    def test_accept(self):
        driver= webdriver.Chrome()

        try:
           URL = "https://the-internet.herokuapp.com/checkboxes"
           driver.get("https://the-internet.herokuapp.com/javascript_alerts")
           driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(1) > button")
           alert = driver.switch_to.alert

           alert.accept()
           assert  driver.find_element(By.ID, "result").text == "You successfully clicked an alert"

        finally:
            driver.quit()

    # def test_sum_some_negative(self):
    #     resultado = suma(1, -2)
    #     self.assertEqual(resultado, -1)


if __name__ == '__main__':
    # unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
