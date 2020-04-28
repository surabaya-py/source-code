from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(30)

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

driver.find_element_by_id("txtUsername").send_keys("admin")

driver.find_element_by_id("txtPassword").send_keys("admin123")

driver.find_element_by_name("Submit").click()

driver.find_element_by_xpath("//div[@id='content']/div/div[2]").click()

# driver.close()
print("Test Complete")
