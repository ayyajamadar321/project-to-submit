from selenium.webdriver.common.by import By


class registrationPage:
    def __init__(self, driver):
        self.driver = driver

    registrationbutton_ele = (By.XPATH, "//a[@class='nav-link btn-xs btn btn-primary']")
    name_ele = (By.CSS_SELECTOR, "input#fname")
    lastname_ele = (By.XPATH, "//input[@id='lname']")
    phoneno_ele = (By.NAME, "phoneNumber")
    email_ele = (By.XPATH, "//input[@id='email']")
    password_ele = (By.XPATH, "//input[@id='password']")
    confpassword_ele = (By.XPATH, "//input[@id='password_confirm']")
    checkbox_ele = (By.CSS_SELECTOR, "div.u-check-icon-checkbox-v4")
    register_ele = (By.XPATH, "//button[@id='register-button']")
    verify_msg = (By.ID, "global-error-login")

    def get_registrationbutton(self):
        return self.driver.find_element(*registrationPage.registrationbutton_ele)

    def get_name(self):
        return self.driver.find_element(*registrationPage.name_ele)

    def get_lastname(self):
        return self.driver.find_element(*registrationPage.lastname_ele)

    def get_phoneno(self):
        return self.driver.find_element(*registrationPage.phoneno_ele)

    def get_email(self):
        return self.driver.find_element(*registrationPage.email_ele)

    def get_password(self):
        return self.driver.find_element(*registrationPage.password_ele )

    def get_confpassword(self):
        return self.driver.find_element(*registrationPage.confpassword_ele)

    def get_checkbox(self):
        return self.driver.find_element(*registrationPage.checkbox_ele)

    def get_register(self):
        return self.driver.find_element(*registrationPage.register_ele)

    def get_verify_msg(self):
        return self.driver.find_element(*registrationPage.verify_msg)