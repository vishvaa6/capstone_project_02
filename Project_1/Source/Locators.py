


class Locators:

#---------------------------------- TC_LOGIN AND LOGOUT -------------------------------------#

    # FOR LOGIN LOCATORS

    user_input_username = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
    user_input_password = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
    login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    invalid_message = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'



    # FOR LOGOUT LOCATORS

    logout_menu = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span'
    logout_button = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]'

#---------------------------------- MENU_LOCATORS -------------------------------------#


    menu_PIM = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'


#---------------------------------- PIM_LOCATORS -------------------------------------#

    #FOR EMPLOYEE LIST

    pim_add_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    pim_employee_name_input = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    pim_employee_id = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input'
    pim_employee_status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div'
    pim_employee_status_value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]'
    pim_include = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div'
    pim_include_value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]'
    pim_supervisor_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[5]/div/div[2]/div/div/input'
    pim_job_title = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div'
    pim_job_title_value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[2]'
    pim_sub_unit = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[7]/div/div[2]/div/div'
    pim_sub_unit_value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[7]/div/div[2]/div/div[2]/div[3]'



    #FOR ADD USER

    pim_add_user = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    pim_first_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
    pim_middle_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
    pim_last_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
    pim_id = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    pim_profile = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div'
    pim_save = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    pim_success_message = '//*[@id="oxd-toaster_1"]/div/div[1]/div[2]/p[2]'



    pim_search = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    pim_edit_user = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]'
    pim_add_middle_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input'
    pim_other_id = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    pim_ssn_num = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div[2]/input'
    pim_driver_license_num = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    pim_license_expiry_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    pim_expiry_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[25]/div'
    pim_nationality = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div'
    pim_nationality_india = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[84]'
    pim_marital_status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i'
    pim_marital_status_india = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]'
    pim_dob = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    pim_gender_male = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label'
    pim_save_profile = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
    pim_success_edit_message = '//*[@id="oxd-toaster_1"]/div/div[1]/div[2]/p[2]'
    pim_delete_user = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]'
    pim_confirm_delete = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
    pim_successfully_deleted = '//*[@id="oxd-toaster_1"]/div/div[1]/div[2]/p[2]'
