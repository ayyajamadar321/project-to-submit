import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class base:
    def explicitwait(self, locator):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(locator))

    def selectOptipn(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)