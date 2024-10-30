from Browser.StartStop import StartStop
from TC_LOGIN_01.Login import LoginTest
from TC_LOGIN_02.Negative_Login import NegativeLoginTest
from TC_PIM_01.AddUser import AddUser
from TC_PIM_02.EditUser import EditUser
from TC_PIM_03.DeleteUser import DeleteUser

def test_start():
    assert StartStop().start() == True
    print("automation Started")



def test_login():
    assert LoginTest().login() == True
    print("TC_LOGIN_01 POSITIVE : The User is Logged in Successfully")

def test_logout():
    assert LoginTest().logout() == True
    print("TC_LOGIN_01 POSITIVE :User Logged Out Successfully")



def test_negative_login():
    assert NegativeLoginTest().negative_login() == True
    print("TC_LOGIN_02 NEGATIVE : The Invalid error Message is Displayed")


def test_add_user():
    assert AddUser().add_user() == "Successfully Saved"
    print("TC_PIM_01 POSITIVE : The User Should be able to ADD an new employee in the PIM")

def test_edit_user ():
    assert EditUser().edit_user() == "Successfully Updated"
    print("TC_PIM_02 POSITIVE : The User Should be able to EDIT an Existing employee information in PIM")

def test_delete_user():
    assert DeleteUser().delete_user() == "Successfully Deleted"
    print("TC_PIM_03 POSITIVE : The User Should be able to DELETE an Existing employee information in PIM")
