from selenium.webdriver.common.by import By


class dashboardPage:
    def __init__(self, driver):
        self.driver = driver

    profile_ele = (By.XPATH, "//span[contains(text(),'Profile')]")
    about_ele = (By.XPATH, "//a[contains(text(),'About')]")
    name_ele = (By.CSS_SELECTOR, "input#fname")  # First name
    last_ele = (By.XPATH, "//input[@name='lname']")  # last name
    gender_ele = (By.XPATH, "//select[@id='gender']")  # gender
    COB_ele = (By.XPATH, "//select[@id='birth_country']")  # birth_country
    Nationality_ele = (By.XPATH, "//select[@id='nationality']")  # nationality
    phoneNumber_ele = (By.NAME, "phonenumber")  # phonenumber
    city_ele = (By.XPATH, "//input[@name='city']")  # city
    Address_ele = (By.XPATH, "//textarea[@name='streetadd']")  # Address
    state_ele = (By.XPATH, "//input[@name='state']")  # state
    zipcode_ele = (By.XPATH, "//input[@name='zipcode']")  # zipcode
    dob_ele = (By.XPATH, "//input[@id='dob']")  # dob
    Save_ele = (By.XPATH, "//button[contains(text(),'Save & Next')]")  # Save

    def get_profile(self):
        return self.driver.find_element(*dashboardPage.profile_ele)

    def get_about(self):
        return self.driver.find_element(*dashboardPage.about_ele)

    def get_name(self):
        return self.driver.find_element(*dashboardPage.name_ele)

    def get_last(self):
        return self.driver.find_element(*dashboardPage.last_ele)

    def get_gender(self):
        return self.driver.find_element(*dashboardPage.gender_ele)

    def get_COB(self):
        return self.driver.find_element(*dashboardPage.COB_ele)

    def get_Nationality(self):
        return self.driver.find_element(*dashboardPage.Nationality_ele)

    def get_phoneNumber(self):
        return self.driver.find_element(*dashboardPage.phoneNumber_ele)

    def get_city(self):
        return self.driver.find_element(*dashboardPage.city_ele)

    def get_Address(self):
        return self.driver.find_element(*dashboardPage.Address_ele)

    def get_state(self):
        return self.driver.find_element(*dashboardPage.state_ele)

    def get_zipcode(self):
        return self.driver.find_element(*dashboardPage.zipcode_ele)

    def get_dob(self):
        return self.driver.find_element(*dashboardPage.dob_ele)

    def get_Save(self):
        return self.driver.find_element(*dashboardPage.Save_ele)
