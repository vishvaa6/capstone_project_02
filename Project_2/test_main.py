from TC_1.ForgotPassword import ForgotPassword
from TC_2.HeaderValidation import HeaderValidation
from TC_3.MenuValidation import MenuValidation
from Browser.StartStop import StartStop

#---------------------------- TEST_CASE_01-----------------------------#

def test_start():
    assert StartStop().start() == True
    print("automation started")

def test_forgot_password():
    assert ForgotPassword().forgot_password() == True
    print("TEST_CASE_01 : SUCCESS : The Username Box is visible")

def test_reset_pass_notification():
    assert ForgotPassword().reset_pass_notification() == "Reset Password link sent successfully"
    print("TEST_CASE_01 : SUCCESS : Reset Password link sent successfully ")

#---------------------------- TEST_CASE_02-----------------------------#

def test_start2():
    assert StartStop().start() == True
    print("TEST_CASE_02 : automation started")

def test_log():
    assert HeaderValidation().login() == True
    print("TEST_CASE_02 : Login Successfully")

def test_head():
    assert HeaderValidation().title() == "OrangeHRM"
    print("TEST_CASE_02 : Title Validation is successful")

def test_user_management():
    assert HeaderValidation().user_manage() == True
    print("TEST_CASE_02 : User Management Tab is Visible")

def test_job_tab():
    assert HeaderValidation().job_tab() == True
    print("TEST_CASE_02 : job Tab is Visible")

def test_organization_tab():
    assert HeaderValidation().organization_tab() == True
    print("TEST_CASE_02 : organization Tab is Visible")

def test_qualification_tab():
    assert HeaderValidation().qualification_tab() == True
    print("TEST_CASE_02 : Qualification Tab is Visible")

def test_nationalities_tab():
    assert HeaderValidation().nationalities_tab() == True
    print("TEST_CASE_02 : nationalities Tab is Visible")

def test_corporate_branding_tab():
    assert HeaderValidation().corporate_branding_tab() == True
    print("TEST_CASE_02 : corporate_branding Tab is Visible")

def test_configuration_tab():
    assert HeaderValidation().configuration_tab() == True
    print("TEST_CASE_02 : configuration Tab is Visible")

#---------------------------- TEST_CASE_03-----------------------------#

def test_admin():
    assert MenuValidation().admin() == 'Admin'
    print("TEST_CASE_03 : SUCCESS : Admin tab is visible")

def test_pim():
    assert MenuValidation().pim() == 'PIM'
    print("TEST_CASE_03 : SUCCESS : PIM tab is visible")


def test_leave():
    assert MenuValidation().leave() == 'Leave'
    print("TEST_CASE_03 : SUCCESS : lEAVE tab is visible")


def test_time():
    assert MenuValidation().time() == 'Time'
    print("TEST_CASE_03 : SUCCESS : TIME tab is visible")


def test_recruitment():
    assert MenuValidation().recruitment() == 'Recruitment'
    print("TEST_CASE_03 : SUCCESS : RECRUITMENT tab is visible")


def test_my_info():
    assert MenuValidation().my_info() == 'My Info'
    print("TEST_CASE_03 : SUCCESS : MY INFO tab is visible")


def test_performance():
    assert MenuValidation().performance() == 'Performance'
    print("TEST_CASE_03 : SUCCESS : PERFORMANCE tab is visible")


def test_dashboard():
    assert MenuValidation().dashboard() == 'Dashboard'
    print("TEST_CASE_03 : SUCCESS : DASHBOARD tab is visible")


def test_directory():
    assert MenuValidation().directory() == 'Directory'
    print("TEST_CASE_03 : SUCCESS : DIRECTORY tab is visible")


def test_maintenance():
    assert MenuValidation().maintenance() == 'Maintenance'
    print("TEST_CASE_03 : SUCCESS : MAINTENANCE tab is visible")

def test_buzz():
    assert MenuValidation().buzz() == 'Buzz'
    print("TEST_CASE_03 : SUCCESS : BUZZ tab is visible")

def test_quit3():
    assert StartStop().quit() == True
    print("TEST_CASE_03 : Automation Stopped")