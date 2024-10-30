from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Source.Data import Data
from Source.Locators import Locators
from Browser.StartStop import StartStop


class EditUser(Data,Locators):

    wait = StartStop().TimeOut
    driver = StartStop().WebDriverChrome


    def edit_user(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.menu_PIM))).click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_employee_name_input))).send_keys("Ganesh")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_search))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_edit_user))).click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_add_middle_name))).send_keys("kumar")
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_other_id))).send_keys("567899243")
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_driver_license_num))).send_keys("KA0419920009646")

        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_license_expiry_date))).send_keys("2028-12-08")
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_nationality))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_nationality_india))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_marital_status))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_marital_status_india))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_dob))).send_keys("2004-14-09")
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_gender_male))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_save_profile))).click()
        if self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_success_edit_message))).is_displayed():
            value = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pim_success_edit_message))).text


            return value








