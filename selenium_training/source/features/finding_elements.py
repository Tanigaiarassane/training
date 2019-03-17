from lib.browsertest import Browser
from selenium.webdriver.common.by import By

import time
_id = "name"
_name ="enter-name"

if __name__== "__main__":
    f = Browser()
    f.fetch_url(url="https://letskodeit.teachable.com/pages/practice")
    time.sleep(3)
    elements_by_tag = f.driver.find_elements(By.TAG_NAME, "tr")
    if elements_by_tag:
        print "Number of tr tags {}".format(len(elements_by_tag))
    f.diconnect()