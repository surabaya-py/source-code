# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import HtmlTestRunner

class Test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # self.base_url = "https://www.google.com/"

    def test_2(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/dashboard")
        # driver.find_element_by_id("txtUsername").click()
        # driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        # driver.find_element_by_id("txtPassword").click()
        # driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        # driver.implicitly_wait(50)
        driver.find_element_by_xpath("//div[@id='content']/div/div[2]").click()

    # def tearDown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    # unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
