import unittest
from selenium import webdriver
from faker import Faker
from pages.login_page import *
from resources.data import LoginPageData
from resources.drivers import *


class LoginPageTests(unittest.TestCase):
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

    def test_login_correct(self):
        login_page = LoginPage(self.driver)
        login_page.login(LoginPageData.USERNAME, LoginPageData.PASSWORD)

    def test_login_incorrect(self):
        login_page = LoginPage(self.driver)
        login_page.login('username', 'password!')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
