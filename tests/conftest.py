import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from utilities.readProperties import ReadConfig


@pytest.fixture
def setup(request):  # Run befor and after test case
    browserName = "chrome"

    if browserName == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browserName == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    elif browserName == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())

    else:
        print("Please select the browser")

    driver.get(ReadConfig.getApplicationUrl())  # url address
    print(driver.title)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(15)
    request.cls.driver = driver
    yield
    driver.close()
