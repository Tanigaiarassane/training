"""
Driver property and methods
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get()
    driver.title
    driver.current_url
    driver.refresh()
    driver.get(driver.current_url)
    driver.back()
    driver.forward()
    driver.page_source
    driver.close()
    driver.quit()
"""
from lib.browsertest import Browser
import time

if __name__== "__main__":
    browser = Browser()
    browser.driver.maximize_window()
    browser.driver.get("http://td3-activity.herokuapp.com/login")
    print "URL : {}".format(browser.driver.current_url)
    browser.driver.get(browser.driver.current_url)
    browser.driver.back()
    browser.driver.forward()
    print "Page source : {}".format(browser.driver.page_source)
    time.sleep(3)
    browser.driver.quit()