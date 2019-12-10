import unittest
from selenium import webdriver
from faker import Faker
from pages.login_page import *
from pages.home_page import *
from resources.data import *
from resources.drivers import *


class HomePageTests(unittest.TestCase):
    def setUp(self):
        ##
        # Konfiguracja Faker'a
        ##
        self.fake = Faker('pl_PL')

        ##
        # Konfiguracja WebDrivera
        ##
        firefox_driver = Driver()
        self.driver = firefox_driver.driver

        login_page = LoginPage(self.driver)
        login_page.login(LoginPageData.USERNAME, LoginPageData.PASSWORD)

    def test_open_form_fill_page(self):
        home_page = HomePage(self.driver)
        home_page.click_form_fill_button()

        self.assertIn('Wyszukiwanie ankiety klienta', self.driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
