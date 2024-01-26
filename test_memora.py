from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import unittest

creds = {
    "email": "dbernal@outpostqa.com",
    "password": "MemoraOutpostQA123."
}


class Memora_addPatient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_create_patient(self):
        # Login
        self.driver.get("https://sandbox.memorahealth.com/")
        element = self.driver.find_element(By.XPATH, "//input[@type='email']")
        element.send_keys(creds['email'])
        element = self.driver.find_element(By.XPATH, "//input[@type='password']")
        element.send_keys(creds['password'])
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(4)

        # Add Patient
        self.driver.find_element(By.XPATH, "//span[text()='Add Patient']").click()
        element = self.driver.find_element(By.ID, "First Name")
        element.send_keys("Selenium")
        element = self.driver.find_element(By.ID, "Last Name")
        element.send_keys("Patient")
        element = self.driver.find_element(By.XPATH, "//input[@type='tel']")
        element.send_keys(f"4085{random.randint(100000, 999999)}")
        self.driver.find_element(By.XPATH, "//div[text()='Select a Physician *']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Tyler Newman']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Select an Address *']").click()
        self.driver.find_element(By.XPATH, "//div[text()='OutpostQA Clinic']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Care Teams *']").click()
        self.driver.find_element(By.XPATH, "//div[text()='OutpostQA Care']").click()
        self.driver.find_element(By.XPATH, "//input[@name='dob']").send_keys("12121212")
        self.driver.find_element(By.XPATH, "//span[text()='Save']").click()
        time.sleep(4)

    def test_02_send_survey(self):
        self.driver.find_element(By.XPATH, "//button[@aria-label='Open patient live chat']").click()
        textbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='Compose_compose-main__NVz3X']"))
            and EC.visibility_of_element_located((By.XPATH, "//div[@class='Compose_compose-main__NVz3X']"))
        )
        textbox.click()
        message = "Holis, aqui te va una encuesta:"
        self.driver.find_element(By.XPATH, "//textarea[contains(@class, 'MuiInputBase-input') "
                                           "and contains(@class, 'MuiInputBase-inputMultiline') "
                                           "and contains(@class, '_ar_hide_')]").send_keys(message)
        self.driver.find_element(By.XPATH, "//button[contains(@data-testid, 'send-message-button')]").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Live chat - Open patient resources')]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Selenium Test Survey']").click()
        self.driver.find_element(By.XPATH, ".//span[text()='Send']").click()
        time.sleep(5)


    def test_03_delete_patient(self):
        self.driver.find_element(By.XPATH, "//button[@title='Delete']").click()
        self.driver.find_element(By.XPATH, ".//span[text()='Delete']").click()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("\nDone")


if __name__ == '__main__':
    unittest.main()
