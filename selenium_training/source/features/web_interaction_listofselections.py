"""
Element property and methods
     element.clear()
     element.click()
     element.send_keys()
"""
from lib.browsertest import Browser
from selenium.webdriver.common.by import By

import time

if __name__== "__main__":
    browser = Browser()
    browser.driver.maximize_window()
    browser.driver.get("https://learn.letskodeit.com/p/practice")
    browser.driver.implicitly_wait(3)
    car_radio_btns = browser.driver.find_elements(By.XPATH,"//input[contains(@type,'radio') and contains(@name,'cars')]")
    print len(car_radio_btns)
    time.sleep(3)

    for radio_buttons in car_radio_btns:
        if not radio_buttons.is_selected():
            radio_buttons.click()
            time.sleep(3)

    browser.driver.quit()