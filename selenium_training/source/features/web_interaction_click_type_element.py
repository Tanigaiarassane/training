"""
Element property and methods
     element.clear()
     element.click()
     element.send_keys()
"""
from lib.browsertest import Browser
import time

if __name__== "__main__":
    browser = Browser()
    browser.driver.maximize_window()
    browser.driver.get("http://td3-activity.herokuapp.com/login")
    browser.driver.implicitly_wait(10)
    email = browser.get_element("xpath","//input[@id='email']")
    email.send_keys("tanigai.dj@gmail.com")
    password = browser.get_element("xpath", "//input[@id='password']")
    password.send_keys("tanigai@123")
    submit = browser.get_element("xpath","//input[@id='submit']")
    submit.click()
    time.sleep(3)
    browser.driver.quit()