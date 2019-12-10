import unittest
from selenium import webdriver
from faker import Faker
import datetime
from pages.login_page import *
from pages.poll_page import *
from pages.home_page import *
from resources.data import *
from resources.drivers import *


class PollPageTests(unittest.TestCase):
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

        home_page = HomePage(self.driver)
        home_page.click_form_fill_button()

    def test_invest_poll_positive_and_invest_poll_positive(self):
        birth_date = self.fake.date_between_dates(date_start=datetime.date(1990, 9, 6), date_end=datetime.date(1999, 9, 9))
        pesel = self.fake.pesel(date_of_birth=birth_date, sex=None)
        birth_date2 = self.fake.date_between_dates(date_start=datetime.date(1990, 9, 6), date_end=datetime.date(1999, 9, 9))
        pesel2 = self.fake.pesel(date_of_birth=birth_date, sex=None)

        poll_page = PollPage(self.driver)
        poll_page.choose_is_the_same_person(False)
        poll_page.click_next_button()
        poll_page.choose_insurer_protective_type(2)
        poll_page.enter_insurer_nationality('Polskie')
        poll_page.enter_insurer_pesel(pesel)
        poll_page.click_next_button()
        poll_page.accept_alert()
        poll_page.click_start_fill_poll()
        poll_page.click_fill_poll(2)
        poll_page.enter_name_poll_form('Piotr')
        poll_page.enter_surname_poll_form('Szewczyk')
        poll_page.enter_nationality_poll_form('Polskie')
        poll_page.enter_pesel_poll_form(pesel)
        poll_page.enter_birth_date_poll_form(birth_date)
        poll_page.enter_id_card_type_poll_form('Dowód osobisty')
        poll_page.enter_id_card_number_poll_form('AYC667623')
        poll_page.choose_fill_poll(True)
        poll_page.choose_agreement_1(True)
        poll_page.choose_agreement_2(True)
        poll_page.click_next_button()
        poll_page.fill_l6_invest_positive_rec_poll(
            q2=3,
            q3=3,
            q4=(3, 3),
            q5=7,
            q6=89,
            q10=3,
            q11=5,
            q12=94,
            q13=(True, True),
            q14=5,
            q7=5,
            q8=(2, 2, 1, 1, 1, 1),
            q9=(1, 2, 2, 1))
        poll_page.click_next_button()
        poll_page.choose_insured_protective_type(2)
        poll_page.enter_insured_nationality('Polskie')
        poll_page.enter_insured_pesel(pesel2)
        poll_page.click_next_button()
        poll_page.accept_alert()
        poll_page.click_start_fill_poll()
        poll_page.click_fill_poll(2)
        poll_page.enter_name_poll_form('Piotr')
        poll_page.enter_surname_poll_form('Szewczyk')
        poll_page.enter_nationality_poll_form('Polskie')
        poll_page.enter_pesel_poll_form(pesel2)
        poll_page.enter_birth_date_poll_form(birth_date2)
        poll_page.enter_id_card_type_poll_form('Dowód osobisty')
        poll_page.enter_id_card_number_poll_form('AYC667623')
        poll_page.choose_fill_poll(True)
        poll_page.choose_agreement_1(True)
        poll_page.choose_agreement_2(True)
        poll_page.click_next_button()
        poll_page.fill_l6_invest_positive_rec_poll(
            q2=3,
            q3=3,
            q4=(3, 3),
            q5=7,
            q6=89,
            q10=3,
            q11=5,
            q12=94,
            q13=(True, True),
            q14=5,
            q7=5,
            q8=(2, 2, 1, 1, 1, 1),
            q9=(1, 2, 2, 1))
        poll_page.click_next_button()

    def tearDown(self):
        pass
        # self.driver.close()


if __name__ == "__main__":
    unittest.main()
