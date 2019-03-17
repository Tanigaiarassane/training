from lib.browsertest import Browser
import time
_id = "name"
_name ="enter-name"

if __name__== "__main__":
    f = Browser()
    f.fetch_url(url="https://letskodeit.teachable.com/pages/practice")
    time.sleep(3)
    element_by_xpath = f.driver.find_element_by_xpath("//input[@id='name']")
    if element_by_xpath:
        print "Found the element by Xpath"

    element_by_css = d=f.driver.find_element_by_css("#name")
    if element_by_css:
        print "Found an element by CSS"
    time.sleep(3)
    f.diconnect()