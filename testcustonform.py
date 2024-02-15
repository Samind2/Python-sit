from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest

class TestCustomerForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")

    def test_input1(self):
        self.driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = self.driver.find_element(By.ID, "firstName")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        drp_title = Select(self.driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("canonc")
        age.send_keys("2")

        submit = self.driver.find_element(By.ID, "submit")
        submit.click()

        time.sleep(1) # Give some time for the page to update
        
        result = self.driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjohn", result)

    def tearDown(self):
        self.driver.save_screenshot('testjhone11.png')
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
