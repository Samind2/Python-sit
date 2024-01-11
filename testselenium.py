from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest

class GoogleTest(unittest.TestCase):
    
    def setUp(self):
        s = Service('D:\webdriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)   

    def tearDown(self):
        self.driver.quit()

    def test_search_by_keyword(self):
        self.driver.get("http://www.google.com")
        search_box = self.driver.find_element(By.NAME,"q")
        search_box.send_keys("PBRU")
        search_box.send_keys(Keys.RETURN)
        print(self.driver.title)
        page_content = self.driver.page_source
        self.assertIn("PBRU", page_content, "Not in Page")

if __name__ == "__main__":
    unittest.main()
