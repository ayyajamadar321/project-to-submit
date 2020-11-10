from datetime import datetime
import pytest
from pageObjects.loginPage import loginPage
from testdata.data import Data
from utilities.utiliti import base


class Testloginpage(base):

    def test_loginpage(self, get_data):  # Test Case for login function
        logIn = loginPage(self.driver)
        try:
            logIn.get_loginButton().click()
            logIn.get_username().send_keys(get_data["username"])
            logIn.get_password().send_keys(get_data["password"])
            logIn.get_submit().click()
        except Exception as e:
            print(e)
        finally:
            now = datetime.now()
            current_time = now.strftime("%H-%M-%S")
            self.driver.save_screenshot('..\\screenshots\\loginTest' + current_time + '.png')

    @pytest.fixture(params=Data.loginpage_Data)  # To fetch data from Data class(parametrisation)
    def get_data(self, request):
        return request.param
