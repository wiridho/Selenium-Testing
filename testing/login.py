import unittest
import time
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    def test_success_login(self):
        baseUrl = "https://practicetestautomation.com"
        driver = self.browser
        driver.get(baseUrl+'/practice-test-login')
        driver.find_element(By.ID, "username").send_keys("student") #input username
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("Password123") #input password
        time.sleep(1)
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
    def test_negative_username_login(self):
        baseUrl = "https://practicetestautomation.com"
        driver = self.browser
        driver.get(baseUrl+'/practice-test-login')
        driver.find_element(By.ID, "username").send_keys("thisIsWrongUsername")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("Password123")
        time.sleep(1)
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, "error").text
        self.assertIn("Your username is invalid!", error_message)
    def test_negative_password_login(self):
        baseUrl = "https://practicetestautomation.com"
        driver = self.browser
        driver.get(baseUrl+'/practice-test-login')
        driver.find_element(By.ID, "username").send_keys("student") #username
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("thisIsWrongPass") #password
        time.sleep(1)
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, "error").text
        self.assertIn("Your password is invalid!", error_message)

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)