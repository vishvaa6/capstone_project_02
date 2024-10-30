from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Source.Data import Data
from Source.Locators import Locators
from Browser.StartStop import StartStop




class AddUser(Data,Locators):
    wait = StartStop().TimeOut
    driver = StartStop().WebDriverChrome



    def add_user(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_input_username))).send_keys(self.username)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_input_password))).send_keys(self.password[0])
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button))).click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_PIM))).click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_add_user))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_first_name))).send_keys("Ganesh")
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_middle_name))).send_keys("")
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_last_name))).send_keys("k")
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_id))).send_keys("7676")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_save))).click()
        if self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_success_message))).is_displayed():
            value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_success_message))).text

            return value