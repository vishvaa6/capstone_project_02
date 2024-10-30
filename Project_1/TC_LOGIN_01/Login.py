from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Source.Data import Data
from Source.Locators import Locators
from Browser.StartStop import StartStop






class LoginTest(Data,Locators):
     wait = StartStop().TimeOut
     driver = StartStop().WebDriverChrome



     def login(self):
          self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_input_username))).send_keys(self.username)
          self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_input_password))).send_keys(self.password[0])
          self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button))).click()
          return True

     def logout(self):
          self.wait.until(EC.presence_of_element_located((By.XPATH,self.logout_menu))).click()
          self.wait.until(EC.presence_of_element_located((By.XPATH,self.logout_button))).click()
          return True