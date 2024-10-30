
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Source.Data import Data
from Source.Locators import Locators
from Browser.StartStop import StartStop






class NegativeLoginTest(Data,Locators):
     wait = StartStop().TimeOut
     driver = StartStop().WebDriverChrome



     def negative_login(self):
          self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_input_username))).send_keys(self.username)
          self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_input_password))).send_keys(self.password[1])
          self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button))).click()
          self.wait.until(EC.presence_of_element_located((By.XPATH,self.invalid_message))).is_displayed()

          return True



