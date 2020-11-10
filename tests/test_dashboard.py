# import time
# from datetime import datetime
#
# import pytest
# from pageObjects.dashboardPage import dashboardPage
# from pageObjects.loginPage import loginPage
# from testdata.data import Data
# from utilities.readProperties import ReadConfig
# from utilities.utiliti import base
#
#
# class TestDashboardpage(base):
#
#     def test_dashboardpage(self, get_data):  # Test case for Dashboard page
#
#         board = dashboardPage(self.driver)
#         logIn = loginPage(self.driver)
#         logIn.get_loginButton().click()
#         logIn.get_username().send_keys(ReadConfig.get_oldUsername())
#         logIn.get_password().send_keys(ReadConfig.get_oldPassword())
#         logIn.get_submit().click()
#         board.get_profile().click()
#         # time.sleep(2)
#         board.get_about().click()
#
#         profile_name = board.get_name()
#         profile_name.clear()
#         profile_name.send_keys(ReadConfig.getName())
#
#         profile_lastname = board.get_last()
#         profile_lastname.clear()
#         profile_lastname.send_keys(ReadConfig.getLastName())
#
#         self.selectOptipn(board.get_gender(), get_data["Gender"])
#         self.selectOptipn(board.get_COB(), get_data["COB"])
#         self.selectOptipn(board.get_Nationality(), get_data["Nationality"])
#
#         profile_mobnumber = board.get_phoneNumber()
#         profile_mobnumber.clear()
#         profile_mobnumber.send_keys(ReadConfig.getPhoneNo())
#
#         profile_add = board.get_Address()
#         profile_add.clear()
#         profile_add.send_keys(get_data["Address"])
#
#         profile_state = board.get_state()
#         profile_state.clear()
#         profile_state.send_keys(get_data["State"])
#
#         profile_zipcode = board.get_zipcode()
#         profile_zipcode.clear()
#         profile_zipcode.send_keys(get_data["Zipcode"])
#
#         profile_city = board.get_city()
#         profile_city.clear()
#         profile_city.send_keys(get_data["City"])
#
#         DOB = board.get_dob()
#         DOB.clear()
#         DOB.send_keys(get_data["DOB"])
#         now = datetime.now()
#         current_time = now.strftime("%H-%M-%S")
#         self.driver.save_screenshot('..\\screenshots\\dashboardTest' + current_time + '.png')
#
#     @pytest.fixture(params=Data.Dahboard_Data)  # use param whenever you send data
#     def get_data(self, request):
#         return request.param
