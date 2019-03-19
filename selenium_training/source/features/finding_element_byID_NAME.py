from lib.browsertest import Browser
import time
_id = "name"
_name ="enter-name"

if __name__== "__main__":
    f = Browser()
    f.fetch_url(url="https://letskodeit.teachable.com/pages/practice")
    time.sleep(3)
    element_by_id = f.driver.find_element_by_id(_id)
    if element_by_id:
        print "Found the element by id"

    element_by_name = d=f.driver.find_element_by_name(_name)
    if element_by_name:
        print "Found an element by Name"
    time.sleep(3)
    f.diconnect()