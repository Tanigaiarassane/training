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
    browser.driver.get("http://www.google.com")
    browser.driver.implicitly_wait(10)
    search = browser.get_element("xpath","//input[@role='combobox']")
    print search.is_enabled()
    search.send_keys("tanigai.dj@gmail.com")
    time.sleep(3)
    browser.driver.quit()