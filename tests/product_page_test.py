import unittest
import json
from time import sleep
from faker import Faker
from pages.login_page import *
from pages.home_page import *
from pages.product_search_page import *
from pages.product_edit_page import *
from resources.drivers import *
from resources.data import *


class ProductPageTests(unittest.TestCase):
    def setUp(self):
        # Konfiguracja Faker'a
        self.fake = Faker('pl_PL')

        # Konfiguracja WebDrivera
        firefox_driver = Driver()
        self.driver = firefox_driver.driver

        login_page = LoginPage(self.driver)
        login_page.login(LoginPageData.USERNAME, LoginPageData.PASSWORD)

    def test_add_or_edit_product_all_subscriptions_params(self):
        with open('json/products.json', 'r') as json_file:
            data = json.load(json_file)

        for x in data:
            home_page = HomePage(self.driver)
            home_page.click_product_search_button()

            search_product = SearchProductPage(self.driver)
            search_product.enter_product_symbol(x['symbol'])
            search_product.click_search_button()
            search_product.open_product(x['symbol'])
            search_product.click_edit_button()

            edit_product = EditProductPage(self.driver)
            edit_product.click_manage_subscriptions_button()

            subscription_table = edit_product.return_subscriptions_table()
            for subscription in subscription_table:
                edit_product.click_subscription_details_button(subscription)

                for subscription_param in x['addSubscriptionsParams']:
                    edit_product.enter_subscriptions_param_key(subscription_param['key'])
                    edit_product.enter_subscriptions_param_value(subscription_param['value'])
                    edit_product.click_add_param_button()

                edit_product.click_save_subscription_button()
            edit_product.click_save_button()
            edit_product.click_save_button()
            # break

    def test_new(self):
        with open('json/products.json', 'r') as json_file:
            data = json.load(json_file)

        for x in data:
            home_page = HomePage(self.driver)
            home_page.click_product_search_button()

            search_product = SearchProductPage(self.driver)
            search_product.enter_product_symbol(x['symbol'])
            search_product.click_search_button()
            search_product.open_product(x['symbol'])
            search_product.click_edit_button()

            edit_product = EditProductPage(self.driver)
            edit_product.click_manage_orders_button()

            orders_table = edit_product.return_orders_table()
            for order in orders_table:
                if order[3] == "ZMF" and order[7] == "Aktywny":
                    txt = "//table[@id='productList']/tbody/tr[" + str(order[0]+1) + "]/td[8]"
                    tedi = self.driver.find_element(By.XPATH, txt)
                    tedi.find_element(By.PARTIAL_LINK_TEXT, 'Edytuj').click()
                    edit_product.enter_operation_status('Nieaktywny')
                    edit_product.click_save_button()

            # break
            edit_product.click_submit_button()
            edit_product.click_save_button()

    def test_new_another(self):
        # Dyspozycja zmian finansowych
        self.ORDER_CATEGORY = (By.ID, 'orderDefinition.category')
        # Oczekująca na akceptację, Oczekująca na potwierdzenie, W trakcie rejestracji
        self.ORDER_STATUS = (By.ID, 'orderStatus')

        for x in range(500):
            home_page = HomePage(self.driver)
            home_page.click_order_search_button()

            select = Select(self.driver.find_element(*self.ORDER_CATEGORY))
            select.select_by_visible_text('Dyspozycja zmian finansowych')

            select = Select(self.driver.find_element(*self.ORDER_STATUS))
            select.select_by_visible_text('W trakcie rejestracji')

            self.driver.find_element(By.NAME, '_eventId_search').click()

            self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Anuluj').click()
            self.driver.find_element(By.NAME, '_eventId_cancelForm').click()

    def test_new_blebleble(self):
        with open('json/products.json', 'r') as json_file:
            data = json.load(json_file)

        for x in data:
            home_page = HomePage(self.driver)
            home_page.click_product_search_button()

            search_product = SearchProductPage(self.driver)
            search_product.enter_product_symbol(x['symbol'])
            search_product.click_search_button()
            search_product.open_product(x['symbol'])
            search_product.click_edit_button()

            edit_product = EditProductPage(self.driver)
            edit_product.click_manage_orders_button()

            for order in x['newOrders']:
                self.driver.find_element(*edit_product.ADD_NEW_OPERATION_BUTTON).click()

                select = Select(self.driver.find_element(*edit_product.OPERATION_ORDER_DEFINITION_INPUT))
                select.select_by_visible_text(order['order_code'])

                for right_list in order['right_list']:
                    select = Select(self.driver.find_element(*edit_product.OPERATION_ORDER_RIGHT_LIST_INPUT))
                    select.select_by_value(right_list)
                    self.driver.find_element(*edit_product.ADD_TO_LIST_BUTTON).click()

                edit_product.enter_operation_status('Aktywny')

                if order['confirm_request'] == 'true':
                    self.driver.find_element(*edit_product.OPERATION_ORDER_CONFIRM_REQUEST_INPUT).click()

                self.driver.find_element(*(By.NAME, '_eventId_add')).click()

            self.driver.find_element(*(By.NAME, '_eventId_back')).click()
            self.driver.find_element(*(By.NAME, '_eventId_save')).click()
            # break

    def tearDown(self):
        pass  # self.driver.close()


if __name__ == "__main__":
    unittest.main()
