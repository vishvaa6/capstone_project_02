from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Source.Data import Data
from Source.Locators import Locators
from Browser.StartStop import StartStop

class MenuValidation(Data,Locators):

     wait = StartStop().TimeOut
     driver = StartStop().WebDriverChrome



     def login(self):
          self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_input_password))).send_keys(self.password)
          self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_input_username))).send_keys(self.username)
          self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button))).click()
          self.wait.until(EC.presence_of_element_located((By.XPATH, self.Admin_page))).click()
          return True


     def admin(self):
         self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_admin))).is_displayed()
         value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_admin))).text
         return value
     def pim(self):
         self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_PIM))).is_displayed()
         value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_PIM))).text
         return value
     def leave(self):
         self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_leave))).is_displayed()
         value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_leave))).text
         return value
     def time(self):
         self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_time))).is_displayed()
         value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_time))).text
         return value
     def recruitment(self):
         self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_recruitment))).is_displayed()
         value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_recruitment))).text
         return value
     def my_info(self):
         self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_my_info))).is_displayed()
         value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_my_info))).text
         return value
     def performance(self):
         self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_performance))).is_displayed()
         value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_performance))).text
         return value
     def dashboard(self):
         self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_dashboard))).is_displayed()
         value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_dashboard))).text
         return value
     def directory(self):
         self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_directory))).is_displayed()
         value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_directory))).text
         return value
     def maintenance(self):
         self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_maintenance))).is_displayed()
         value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_maintenance))).text
         return value
     def buzz(self):
         self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_buzz))).is_displayed()
         value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_buzz))).text
         return value
