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
    browser.driver.get("https://learn.letskodeit.com/p/practice")
    browser.driver.implicitly_wait(3)
    bmwradio = browser.get_element("id","bmwradio")
    bmwradio.click()
    time.sleep(3)

    benzradio= browser.get_element("id","benzradio")
    benzradio.click()


    time.sleep(3)

    bmwcheck= browser.get_element("id","bmwcheck")
    bmwcheck.click()
    time.sleep(3)

    benzcheck = browser.get_element("id", "benzcheck")
    benzcheck.click()
    time.sleep(3)


    print "benz Radio " + str(benzradio.is_selected())
    print "Bmw Radio " + str(bmwradio.is_selected())

    print "benz Check " + str(benzcheck.is_selected())
    print "Bmw Check " + str(bmwcheck.is_selected())

    time.sleep(10)

    browser.driver.quit()