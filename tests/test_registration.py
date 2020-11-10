from datetime import datetime
from pageObjects.registrationPage import registrationPage
from utilities.readProperties import ReadConfig
from utilities.utiliti import base


class Testregistrationpage(base):

    def test_ragistrationpage(self):  # Test case for registration page
        restration = registrationPage(self.driver)
        restration.get_registrationbutton().click()
        restration.get_name().send_keys(ReadConfig.getName())
        restration.get_lastname().send_keys(ReadConfig.getLastName())
        restration.get_phoneno().send_keys(ReadConfig.getPhoneNo())
        restration.get_email().send_keys(ReadConfig.getUsername())
        restration.get_password().send_keys(ReadConfig.getPassword())
        restration.get_confpassword().send_keys(ReadConfig.getPassword())
        restration.get_checkbox().click()
        restration.get_register().click()
        self.explicitwait(registrationPage.verify_msg)
        now = datetime.now()
        current_time = now.strftime("%H-%M-%S")
        self.driver.save_screenshot('..\\screenshots\\registrationTest' + current_time + '.png')
        verify_msg = restration.get_verify_msg()
        print(verify_msg.text)
        print("account is created")
        assert verify_msg.text == "An activation email has been sent to your email address. Please verify your email " \
                                  "first.", "Account already present "
