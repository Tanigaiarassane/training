from lib.browsertest import Browser
import time
_id = "name"
_name ="enter-name"

if __name__== "__main__":
    f = Browser()
    f.fetch_url(url="https://letskodeit.teachable.com/pages/practice")
    time.sleep(3)
    element_by_class = f.driver.find_element_by_class_name("inputs")
    if element_by_class:
        print "Found the element by class name"
        element_by_class.send_keys("Welcome to class")

    element_by_tag = d=f.driver.find_element_by_tag_name("h1")
    if element_by_tag:
        print "Found an element by Tag name"
        print element_by_tag.text
    time.sleep(3)
    f.diconnect()