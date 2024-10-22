from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Source.Data import Data
from Source.Locators import Locators
from Browser.StartStop import StartStop






class HeaderValidation(Data,Locators):
     wait = StartStop().TimeOut
     driver = StartStop().WebDriverChrome



     def login(self):
          self.driver.maximize_window()
          self.driver.get(self.url)
          self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_input_username))).send_keys(self.username)
          self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_input_password))).send_keys(self.password)
          self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button))).click()
          return True

     def title(self):
          try:
             self.driver.implicitly_wait(10)
             self.wait.until(EC.presence_of_element_located((By.XPATH, self.Admin_page))).click()
             name = self.driver.title
             return name

          except (NoSuchElementException, ElementNotVisibleException) as error:
               return error

     def user_manage(self):
          if self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_management))).is_displayed():
             return True
          else:
               return False
     def job_tab(self):
          if self.wait.until(EC.presence_of_element_located((By.XPATH, self.job))).is_displayed():
             return True
          else:
               return False
     def organization_tab(self):
          if self.wait.until(EC.presence_of_element_located((By.XPATH, self.organization))).is_displayed():
             return True
          else:
               return False

     def qualification_tab(self):
          if self.wait.until(EC.presence_of_element_located((By.XPATH, self.qualification))).is_displayed():
             return True
          else:
               return False

     def nationalities_tab(self):
          if self.wait.until(EC.presence_of_element_located((By.XPATH, self.nationalities))).is_displayed():
             return True
          else:
               return False
     def corporate_branding_tab(self):
          if self.wait.until(EC.presence_of_element_located((By.XPATH, self.corporate_branding))).is_displayed():
             return True
          else:
               return False

     def configuration_tab(self):
          if self.wait.until(EC.presence_of_element_located((By.XPATH, self.configuration))).is_displayed():
             return True
          else:
               return False