from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Source.Data import Data
from Source.Locators import Locators
from Browser.StartStop import StartStop



class ForgotPassword(Data,Locators):

    wait = StartStop().TimeOut
    driver = StartStop().WebDriverChrome

    def forgot_password(self):
         try:

             self.wait.until(EC.presence_of_element_located((By.XPATH, self.forgot_pass))).click()
             self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_inp))).send_keys(self.username)
             visible = self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_inp))).is_displayed()
             self.wait.until(EC.element_to_be_clickable((By.XPATH, self.reset_button))).click()
             return visible


         except Exception as e:
             print(e)

    def reset_pass_notification(self):
         value = self.wait.until(EC.presence_of_element_located((By.XPATH,self.alert_message))).text
         return value
    def quit(self):
         self.driver.quit()
