from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from Source.Data import Data
from Source.Locators import Locators

""" ----- This class is used to start automation,stop automation and simplify WebDriverWait ----- """

class StartStop(Data,Locators):

    WebDriverChrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    TimeOut = WebDriverWait(WebDriverChrome, 10)

    def start(self):
        self.WebDriverChrome.maximize_window()
        self.WebDriverChrome.get(self.url)
        return True

    def quit(self):
        self.WebDriverChrome.quit()
        return True
