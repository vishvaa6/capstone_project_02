from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Source.Data import Data
from Source.Locators import Locators
from Browser.StartStop import StartStop


class DeleteUser(Data,Locators):

    wait = StartStop().TimeOut
    driver = StartStop().WebDriverChrome


    def delete_user(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_PIM))).click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_employee_name_input))).send_keys("Ganesh")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_search))).click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_delete_user))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_confirm_delete))).click()

        if self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_successfully_deleted))).is_displayed():
            value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_successfully_deleted))).text


            return value
