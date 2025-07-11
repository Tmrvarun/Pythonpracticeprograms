from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element("username").send_keys("Admin")

