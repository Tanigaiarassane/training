from lib.browsertest import Browser
import time
_id = "name"
_name ="enter-name"

if __name__== "__main__":
    f = Browser()
    f.fetch_url(url="https://letskodeit.teachable.com/pages/practice")
    time.sleep(3)
    element_by_link_text = f.driver.find_element_by_link_text("Login")
    if element_by_link_text:
        print "Found the element by Link text"

    element_by_p_link_text = d=f.driver.find_element_by_partial_link_text("Log")
    if element_by_p_link_text:
        print "Found an element by Partial link text"
    time.sleep(3)
    f.diconnect()