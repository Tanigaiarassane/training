from lib.browsertest import Browser
from lib.email_read import read_email_from_gmail
import time

"""
https://vm-csmle-dev-ed.lightning.force.com/lightning/r/cscfga__Product_Basket__c/a0X58000009O0dwEAC/view
tdj@demo.com
tanigai@123
"""

class SalesForce(Browser):
    def login(self):
        self.driver.implicitly_wait(20)
        self.driver.get("https://vm-csmle-dev-ed.lightning.force.com/lightning/r/cscfga__Product_Basket__c/a0X58000009O0dwEAC/view")
        username = self.driver.find_element_by_id("username")
        username.send_keys("tdj@demo.com")
        password = self.driver.find_element_by_id("password")
        password.send_keys("tanigai@123")
        self.driver.find_element_by_id("Login").click()
        code = read_email_from_gmail()
        vcode = s.driver.find_element_by_id('emc')
        vcode.send_keys(code)
        s.driver.find_element_by_id("save").click()

if __name__ == "__main__":
    s = SalesForce()
    s.login()
    opportunities = s.driver.find_elements_by_link_text("Opportunities")
    opportunities.click()
