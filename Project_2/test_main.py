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
    print("SUCCESS : -------------- The Username Box is visible --------------")

def test_reset_pass_notification():
    assert ForgotPassword().reset_pass_notification() == "Reset Password link sent successfully"
    print("SUCCESS : -------------- Reset Password link sent successfully --------------")

#---------------------------- TEST_CASE_02-----------------------------#

def test_start2():
    assert StartStop().start() == True
    print("automation started")

def test_log():
    assert HeaderValidation().login() == True
    print("Automation started successfully")

def test_head():
    assert HeaderValidation().title() == "OrangeHRM"
    print("Title Validation is successful")

def test_user_management():
    assert HeaderValidation().user_manage() == True
    print("User Management Tab is Visible")

def test_job_tab():
    assert HeaderValidation().job_tab() == True
    print("job Tab is Visible")

def test_organization_tab():
    assert HeaderValidation().organization_tab() == True
    print("organization Tab is Visible")

def test_qualification_tab():
    assert HeaderValidation().qualification_tab() == True
    print("Qualification Tab is Visible")

def test_nationalities_tab():
    assert HeaderValidation().nationalities_tab() == True
    print("nationalities Tab is Visible")

def test_corporate_branding_tab():
    assert HeaderValidation().corporate_branding_tab() == True
    print("corporate_branding Tab is Visible")

def test_configuration_tab():
    assert HeaderValidation().configuration_tab() == True
    print("configuration Tab is Visible")

#---------------------------- TEST_CASE_03-----------------------------#

def test_admin():
    assert MenuValidation().admin() == 'Admin'
    print("SUCCESS : Admin tab is visible")

def test_pim():
    assert MenuValidation().pim() == 'PIM'
    print("SUCCESS : PIM tab is visible")


def test_leave():
    assert MenuValidation().leave() == 'Leave'
    print("SUCCESS : lEAVE tab is visible")


def test_time():
    assert MenuValidation().time() == 'Time'
    print("SUCCESS : TIME tab is visible")


def test_recruitment():
    assert MenuValidation().recruitment() == 'Recruitment'
    print("SUCCESS : RECRUITMENT tab is visible")


def test_my_info():
    assert MenuValidation().my_info() == 'My Info'
    print("SUCCESS : MY INFO tab is visible")


def test_performance():
    assert MenuValidation().performance() == 'Performance'
    print("SUCCESS : PERFORMANCE tab is visible")


def test_dashboard():
    assert MenuValidation().dashboard() == 'Dashboard'
    print("SUCCESS : DASHBOARD tab is visible")


def test_directory():
    assert MenuValidation().directory() == 'Directory'
    print("SUCCESS : DIRECTORY tab is visible")


def test_maintenance():
    assert MenuValidation().maintenance() == 'Maintenance'
    print("SUCCESS : MAINTENANCE tab is visible")

def test_buzz():
    assert MenuValidation().buzz() == 'Buzz'
    print("SUCCESS : BUZZ tab is visible")

def test_quit3():
    assert StartStop().quit() == True
    print("Automation Stopped")