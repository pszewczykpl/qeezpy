import unittest
from faker import Faker
import json
from examples.RejPy.pages.login_page import *
from examples.RejPy.pages.home_page import *
from examples.RejPy.pages.unit_page import *
from examples.RejPy.resources.drivers import *
from examples.RejPy.resources.data import *


class UnitPageTests(unittest.TestCase):
    def setUp(self):
        # Konfiguracja Faker'a
        self.fake = Faker('pl_PL')

        # Konfiguracja WebDrivera
        firefox_driver = Driver()
        self.driver = firefox_driver.driver

        login_page = LoginPage(self.driver)
        login_page.login(LoginPageData.USERNAME, LoginPageData.PASSWORD)

    def test_edit_unit(self):
        json_file = open('json/units.json')
        data = json.load(json_file)

        for x in data:
            home_page = HomePage(self.driver)
            home_page.click_unit_search_button()

            unit_page = UnitPage(self.driver)
            unit_page.enter_unit_symbol(x['symbol'])
            unit_page.click_search_button()

            if unit_page.is_exists(*unit_page.DETAILS_BUTTON):
                unit_page.click_details_button()
                unit_page.click_edit_button()

                unit_page.enter_unit_details_macro_region(x['editDetails']['macro_region'])
                unit_page.enter_unit_details_region(x['editDetails']['region'])
                unit_page.click_save_button()
            else:
                print("Brak oddziału: " + str(x['symbol']))

    def tearDown(self):
        pass  # self.driver.close()


if __name__ == "__main__":
    unittest.main()
