from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class Page(object):
    PAGE_URL = None

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)

    def select(self, *locator):
        select = Select(self.driver.find_element(*locator))
        return select

    def accept_alert(self):
        obj = self.driver.switch_to.alert
        obj.accept()
        
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def is_exists(self, *locator):
        self.driver.implicitly_wait(1)
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        self.driver.implicitly_wait(10)
        return True
