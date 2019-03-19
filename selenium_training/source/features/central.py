from lib.browsertest import Browser
from selenium.webdriver.common.by import By

import time
_id = "name"
_name ="enter-name"

if __name__== "__main__":
    f = Browser()
    f.fetch_url(url="https://portal-yoda.arubathena.com/platform/login/user")
    time.sleep(3)
    elements_by_id = f.driver.find_element(By.ID, "email")
    if elements_by_id:
        print "Number of tr tags {}".format(elements_by_id)
    f.diconnect()