from selenium.webdriver.common.by import By
from pageObjects.dashboardPage import dashboardPage


class loginPage:
    def __init__(self, driver):
        self.driver = driver

    loginButton_ele = (By.ID, "login-modal")
    username_ele = (By.XPATH, "//form[@id='login_form_main']//input[@name='email']")
    password_ele = (By.XPATH, "//form[@id='login_form_main']//input[@name='password']")
    submit_ele = (By.XPATH, "//form[@id='login_form_main']//button[@name='btn-login']")

    def get_loginButton(self):
        return self.driver.find_element(*loginPage.loginButton_ele)

    def get_username(self):
        return self.driver.find_element(*loginPage.username_ele)

    def get_password(self):
        return self.driver.find_element(*loginPage.password_ele)

    def get_submit(self):
        return self.driver.find_element(*loginPage.submit_ele)