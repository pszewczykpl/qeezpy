from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# Page is serving basic attributes to use in every single Page class
class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def accept_alert(self):
        obj = self.driver.switch_to.alert
        obj.accept()

    def wait_to_be_clickable(self, *locator):
        self.wait.until(EC.element_to_be_clickable(*locator))

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
