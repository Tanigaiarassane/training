import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
time.sleep(2)
driver.get("https://td3-activity.herokuapp.com/login")
time.sleep(2)
driver.find_element_by_id("email").send_keys("tanigai.dj@gmail.com")
driver.find_element_by_id("password").send_keys("tanigai@123")

driver.find_element_by_id("submit").send_keys(Keys.RETURN)

time.sleep(5)

driver.find_element_by_xpath("/html/body/nav/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='navbarTogglerDemo03']/ul[1]/li[2]/a").click()
time.sleep(2)

driver.find_element_by_id("name").send_keys("2. testing using selenium")
driver.find_element_by_id("content").send_keys("2. content for testing using selenium")
driver.find_element_by_id("submit").click()
