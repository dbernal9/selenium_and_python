from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class AmazonSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_capibara(self):
        self.driver.get("https://amazon.com.mx")
        element = self.driver.find_element(By.NAME, "field-keywords")
        element.send_keys("Capibara")
        self.driver.find_element(By.ID, "nav-search-submit-text").click()
        time.sleep(2)

    def test_search_kemonito(self):
        self.driver.get("https://amazon.com.mx")
        element = self.driver.find_element(By.NAME, "field-keywords")
        element.send_keys("ssd")
        self.driver.find_element(By.ID, "nav-search-submit-text").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("\nDone")