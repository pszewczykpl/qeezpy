from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from qeezpy import Page


class SearchProductPage(Page):
    ##
    # SEARCH PRODUCT PAGE
    ##

    # BASIC INFORMATION
    PARTNER_NAME_SELECT = (By.ID, 'partner')
    PRODUCT_NAME_SELECT = (By.ID, 'productName')
    PRODUCT_SYMBOL_SELECT = (By.ID, 'symbol')
    PRODUCT_SYSTEM_PRODUCT_SELECT = (By.ID, 'product')
    PRODUCT_STATUS_SELECT = (By.ID, 'status')
    PRODUCT_CATEGORY_SELECT = (By.ID, 'category')
    PRODUCT_KIND_SELECT = (By.ID, 'kind')
    COMPANY_NAME_SELECT = (By.ID, 'unit')
    PRODUCT_SALE_FROM_DATE_INPUT = (By.ID, 'saleFrom')
    PRODUCT_SALE_TO_DATE_INPUT = (By.ID, 'saleTo')

    # ORDERS
    ORDER_CATEGORY_INPUT = (By.ID, 'orderCategory')
    ORDER_DEFINITION_CODE_INPUT = (By.ID, 'orderDefinitionCode')
    ORDER_DEFINITION_NAME_INPUT = (By.ID, 'orderDefinitionName')
    ORDER_WORKING_NAME_INPUT = (By.ID, 'workingName')
    ORDER_PLACEMENT_SELECT = (By.ID, 'orderPlacement')
    USER_TYPE_SELECT = (By.ID, 'userType')
    FORM_POLICY_TYPE_SELECT = (By.ID, 'formPolicy')

    # BUTTONS
    SEARCH_BUTTON = (By.NAME, '_eventId_search')
    CLEAR_BUTTON = (By.PARTIAL_LINK_TEXT, 'Wyczyść')

    ##
    # PRODUCT DETAILS PAGE
    ##

    # BUTTONS
    EDIT_BUTTON = (By.NAME, '_eventId_edit')
    EXPORT_WITHOUT_DOCS_BUTTON = (By.NAME, '_eventId_exportNoDocuments')
    EXPORT_WITH_DOCS_BUTTON = (By.NAME, '_eventId_export')
    BACK_BUTTON = (By.NAME, '_eventId_back')

    ##
    # SEARCH PRODUCT PAGE
    ##

    # BASIC INFORMATION
    def select_partner_name(self, partner_name):
        select = Select(self.find_element(*self.PARTNER_NAME_SELECT))
        select.select_by_visible_text(partner_name)

    def select_product_name(self, product_name):
        select = Select(self.find_element(*self.PRODUCT_NAME_SELECT))
        select.select_by_visible_text(product_name)

    def select_product_symbol(self, product_symbol):
        select = Select(self.find_element(*self.PRODUCT_SYMBOL_SELECT))
        select.select_by_visible_text(product_symbol)

    def select_product_system_product(self, product_system_product):
        select = Select(self.find_element(*self.PRODUCT_SYSTEM_PRODUCT_SELECT))
        select.select_by_visible_text(product_system_product)

    def select_product_status(self, product_status):
        select = Select(self.find_element(*self.PRODUCT_STATUS_SELECT))
        select.select_by_visible_text(product_status)

    def select_product_category(self, product_category):
        select = Select(self.find_element(*self.PRODUCT_CATEGORY_SELECT))
        select.select_by_visible_text(product_category)

    def select_product_kind(self, product_kind):
        select = Select(self.find_element(*self.PRODUCT_KIND_SELECT))
        select.select_by_visible_text(product_kind)

    def select_company_name(self, company_name):
        select = Select(self.find_element(*self.COMPANY_NAME_SELECT))
        select.select_by_visible_text(company_name)

    def enter_product_sale_from_date(self, date):
        self.find_element(*self.PRODUCT_SALE_FROM_DATE_INPUT).send_keys(date)

    def enter_product_sale_to_date(self, date):
        self.find_element(*self.PRODUCT_SALE_TO_DATE_INPUT).send_keys(date)

    # ORDERS
    def enter_order_category(self, order_category):
        self.find_element(*self.ORDER_CATEGORY_INPUT).send_keys(order_category)

    def enter_order_definition_code(self, order_definition_code):
        self.find_element(*self.ORDER_DEFINITION_CODE_INPUT).send_keys(order_definition_code)

    def enter_order_definition_name(self, order_definition_name):
        self.find_element(*self.ORDER_DEFINITION_NAME_INPUT).send_keys(order_definition_name)

    def enter_order_working_name(self, order_working_name):
        self.find_element(*self.ORDER_WORKING_NAME_INPUT).send_keys(order_working_name)

    def select_order_placement(self, order_placement):
        select = Select(self.find_element(*self.ORDER_PLACEMENT_SELECT))
        select.select_by_visible_text(order_placement)

    def select_user_type(self, user_type):
        select = Select(self.find_element(*self.USER_TYPE_SELECT))
        select.select_by_visible_text(user_type)

    def select_form_policy_type(self, form_policy_type):
        select = Select(self.find_element(*self.FORM_POLICY_TYPE_SELECT))
        select.select_by_visible_text(form_policy_type)

    # BUTTONS
    def click_search(self):
        self.find_element(*self.SEARCH_BUTTON).click()

    def click_clear(self):
        self.find_element(*self.CLEAR_BUTTON).click()

    # SEARCH RESULTS
    def return_products_table(self):
        products = []
        table = self.driver.find_elements(By.XPATH, "//table[@id='results']/tbody/tr")
        i = 0
        for tr in table:
            product = [i]
            td = tr.find_elements(By.TAG_NAME, 'td')
            for cell in td:
                product.append(cell.text)
            products.append(product)
            i = i + 1

        return products

    def open_product(self, symbol):
        self.find_element(By.NAME, symbol).click()

    ##
    # PRODUCT DETAILS PAGE
    ##

    # BUTTONS
    def click_edit(self):
        self.find_element(*self.EDIT_BUTTON).click()

    def click_export_without_docs(self):
        self.find_element(*self.EXPORT_WITHOUT_DOCS_BUTTON).click()

    def click_export_with_docs(self):
        self.find_element(*self.EXPORT_WITH_DOCS_BUTTON).click()

    def click_back(self):
        self.find_element(*self.BACK_BUTTON).click()
