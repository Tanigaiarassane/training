from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

"""
Firefox - download geckodriver and place it in /usr/local/bin/geckodriver
Chrome - download chromedriver from http://chromedriver.chromium.org/downloads, \
         for windows place the windwos executable
         set the webdriver.chrome.driver system variable to point to the driver location
Windows - download IEDriverServer from seleniumhq.org/downlaods - The Internet Explorer Driver Server
         Goto - Settings - Zoomlevel => 100% , otherwise test will fail
          Internet options -> security ->Enable or Disable protected mode in all tabs
Safari - Server location - SELENIUM_SERVER_JAR - should point to the server jar
        
"""

class Browser():

    def __init__(self, type="Firefox"):
        """
        :param type: Browser type - Firefox, Chrome
        :returns handle to the browser
        """
        #Geckodriver location for firefox driver
        self.firefox_driver_location = "/usr/local/bin/geckodriver"
        # Chrome driver location
        self.chrome_driver_location = "/usr/bin/chromedriver"
        #IE Driver location
        self.ie_driver_location = "C:\\Users\\selvi\\drivers\\IEDriverServer.exe"
        #Server driver location for safari
        self.server_jar_location = "/Users/tanigai/training/selenium/drivers/.jar"

        if type == "Firefox":
            self.driver = webdriver.Firefox(executable_path=self.firefox_driver_location)
        elif type == "Chrome":
            os.environ["webdriver.chrome.driver"] = self.chrome_driver_location
            self.driver = webdriver.Chrome(self.chrome_driver_location)
        elif type == "IE":
            os.environ["webdriver.ie.driver"] = self.ie_driver_location
            self.driver = webdriver.Ie(self.ie_driver_location)
        elif type == "Safari":
            os.environ["SELENIUM_SERVER_JAR"]  = self.server_jar_location
            self.driver = webdriver.Safari(quiet=True)


    def fetch_url(self, url="https://www.google.co.in/"):
        return self.driver.get(url)

    def get_element(self, type, value):
        if type == "id":
            element = self.driver.find_element(By.ID, value)
        elif type == "name":
            element = self.driver.find_element(By.NAME, value)
        elif type == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, value)
        elif type == "xpath":
            element = self.driver.find_element(By.XPATH, value)
        elif type == "ltext": # link_text
            element = self.driver.find_element(By.LINK_TEXT, value)
        elif type =="pltext": # partial link text
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
        elif type == "class":
            element = self.driver.find_element(By.CLASS_NAME, value)
        elif type == "tag":
            element = self.driver.find_element(By.TAG_NAME, value)

    def diconnect(self):
        return self.driver.close()


if __name__ == "__main__":
    # tanigai.dj-rm1b@force.com
    # tanigai@123
    f = Browser()
    if f:
        try:
            f.fetch_url(url="https://letskodeit.teachable.com/pages/practice")
            time.sleep(3)
            e = f.get_element("id", "names")
            if e:
                print "Found element by ID"
        finally:
            f.diconnect()
