from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.page import Page


class UnitPage(Page):
    UNIT_PARTNER_NAME_INPUT = (By.ID, 'partner')
    UNIT_TYPE_INPUT = (By.ID, 'type')
    UNIT_NAME_INPUT = (By.ID, 'name')
    UNIT_SYMBOL_INPUT = (By.ID, 'symbol')
    UNIT_REGION_NAME_INPUT = (By.ID, 'regionName')
    UNIT_MACRO_REGION_NAME_INPUT = (By.ID, 'macroRegionName')

    SEARCH_BUTTON = (By.NAME, '_eventId_search')
    CLEAR_BUTTON = (By.PARTIAL_LINK_TEXT, 'Wyczyść')
    DETAILS_BUTTON = (By.PARTIAL_LINK_TEXT, 'Szczegóły')

    BACK_BUTTON = (By.PARTIAL_LINK_TEXT, 'Powrót')
    EDIT_BUTTON = (By.ID, 'linkEdit')
    LOCK_BUTTON = (By.ID, 'lock')

    UNIT_DETAILS_PARTNER_NAME_INPUT = (By.ID, 'unit.partner')
    UNIT_DETAILS_TYPE_UNIT_INPUT = (By.ID, 'typeSelected0')
    UNIT_DETAILS_TYPE_CENTRAL_INPUT = (By.ID, 'typeSelected1')
    UNIT_DETAILS_NAME_INPUT = (By.ID, 'unit.name')
    UNIT_DETAILS_SYMBOL_INPUT = (By.ID, 'unit.symbol')
    UNIT_DETAILS_CENTRAL_NAME_INPUT = (By.ID, 'central.name')
    UNIT_DETAILS_PHONE_INPUT = (By.ID, 'unit.phone')
    UNIT_DETAILS_ALLOWED_IP_INPUT = (By.ID, 'unit.allowedIp')
    UNIT_DETAILS_ADDRESS_STREET_INPUT = (By.ID, 'unit.address.street')
    UNIT_DETAILS_ADDRESS_HOUSE_NUMBER_INPUT = (By.ID, 'unit.address.houseNumber')
    UNIT_DETAILS_ADDRESS_APARTMENT_NUMBER_INPUT = (By.ID, 'unit.address.apartmentNumber')
    UNIT_DETAILS_ADDRESS_POSTAL_CODE_INPUT = (By.ID, 'unit.address.postCode')
    UNIT_DETAILS_ADDRESS_CITY_INPUT = (By.ID, 'unit.address.city')
    UNIT_DETAILS_MACRO_REGION_INPUT = (By.XPATH, "//div[@id='s2id_macroRegion']/a")
    UNIT_DETAILS_REGION_INPUT = (By.XPATH, "//div[@id='s2id_unit.unitRegion']/a")
    UNIT_DETAILS_REGION_SYMBOL_INPUT = (By.ID, 'unit.unitRegion.symbol')

    UNIT_DETAILS_ROLE_INPUT = (By.ID, 'role')
    ADD_ROLE_BUTTON = (By.ID, 'advancedMegaMultiSelectButton')

    SAVE_BUTTON = (By.NAME, '_eventId_edit')
    ADD_BUTTON = (By.NAME, '_eventId_add')
    CANCEL_BUTTON = (By.ID, 'cancel')

    ##
    # Szukaj oddziału
    ##
    def enter_unit_partner_name(self, partner_name):
        select = Select(self.find_element(*self.UNIT_PARTNER_NAME_INPUT))
        select.select_by_visible_text(partner_name)

    def enter_unit_type(self, type):
        select = Select(self.find_element(*self.UNIT_TYPE_INPUT))
        select.select_by_visible_text(type)

    def enter_unit_name(self, name):
        self.find_element(*self.UNIT_NAME_INPUT).send_keys(name)

    def enter_unit_symbol(self, symbol):
        self.find_element(*self.UNIT_SYMBOL_INPUT).send_keys(symbol)

    def enter_unit_region_name(self, name):
        self.find_element(*self.UNIT_REGION_NAME_INPUT).send_keys(name)

    def enter_unit_macro_region_name(self, name):
        self.find_element(*self.UNIT_MACRO_REGION_NAME_INPUT).send_keys(name)

    def click_search_button(self):
        self.find_element(*self.SEARCH_BUTTON).click()

    def click_clear_button(self):
        self.find_element(*self.CLEAR_BUTTON).click()

    def click_details_button(self):
        self.find_element(*self.DETAILS_BUTTON).click()

    ##
    # SZCZEGÓŁY ODDZIAŁU
    ##
    def click_back_button(self):
        self.find_element(*self.BACK_BUTTON).click()

    def click_edit_button(self):
        self.find_element(*self.EDIT_BUTTON).click()

    def click_lock_button(self):
        self.find_element(*self.LOCK_BUTTON).click()

    ##
    # EDYCJA ODDZIAŁU/DODAWANIE NOWEGO ODDZIAŁU
    ##
    def enter_unit_details_partner_name(self, partner_name):
        select = Select(self.find_element(*self.UNIT_DETAILS_PARTNER_NAME_INPUT))
        select.select_by_visible_text(partner_name)

    def click_details_type_unit(self):
        self.find_element(*self.UNIT_DETAILS_TYPE_UNIT_INPUT).click()

    def click_details_type_central(self):
        self.find_element(*self.UNIT_DETAILS_TYPE_CENTRAL_INPUT).click()

    def enter_unit_details_name(self, name):
        self.find_element(*self.UNIT_DETAILS_NAME_INPUT).send_keys(name)

    def enter_unit_details_symbol(self, symbol):
        self.find_element(*self.UNIT_DETAILS_SYMBOL_INPUT).send_keys(symbol)

    def enter_unit_details_central_name(self, name):
        self.find_element(*self.UNIT_DETAILS_CENTRAL_NAME_INPUT).send_keys(name)

    def enter_unit_details_phone(self, phone):
        self.find_element(*self.UNIT_DETAILS_PHONE_INPUT).send_keys(phone)

    def enter_unit_details_allowed_ip(self, ip):
        self.find_element(*self.UNIT_DETAILS_ALLOWED_IP_INPUT).send_keys(ip)

    def enter_unit_details_address_street(self, ip):
        self.find_element(*self.UNIT_DETAILS_ADDRESS_STREET_INPUT).send_keys(ip)

    def enter_unit_details_address_house_number(self, ip):
        self.find_element(*self.UNIT_DETAILS_ADDRESS_HOUSE_NUMBER_INPUT).send_keys(ip)

    def enter_unit_details_address_apartment_number(self, ip):
        self.find_element(*self.UNIT_DETAILS_ADDRESS_APARTMENT_NUMBER_INPUT).send_keys(ip)

    def enter_unit_details_address_postal_code(self, ip):
        self.find_element(*self.UNIT_DETAILS_ADDRESS_POSTAL_CODE_INPUT).send_keys(ip)

    def enter_unit_details_address_city(self, ip):
        self.find_element(*self.UNIT_DETAILS_ADDRESS_CITY_INPUT).send_keys(ip)

    def enter_unit_details_macro_region(self, macro_region):
        self.find_element(*self.UNIT_DETAILS_MACRO_REGION_INPUT).click()
        self.find_element(By.CSS_SELECTOR, "#select2-drop:not([style*='display: none']) .select2-input").send_keys(macro_region)
        self.find_element(By.XPATH, "//div[@class='select2-result-label']/span").click()

    def enter_unit_details_region(self, region):
        self.find_element(*self.UNIT_DETAILS_REGION_INPUT).click()
        self.find_element(By.CSS_SELECTOR, "#select2-drop:not([style*='display: none']) .select2-input").send_keys(region)
        self.find_element(By.XPATH, "//div[@class='select2-result-label']/span").click()

    def enter_unit_details_region_symbol(self, symbol):
        self.find_element(*self.UNIT_DETAILS_REGION_SYMBOL_INPUT).send_keys(symbol)

    def enter_unit_details_role(self, role):
        select = Select(self.find_element(*self.UNIT_DETAILS_ROLE_INPUT))
        select.select_by_visible_text(role)

    def click_add_role_button(self):
        self.find_element(*self.ADD_ROLE_BUTTON).click()

    def click_save_button(self):
        self.find_element(*self.SAVE_BUTTON).click()

    def click_add_button(self):
        self.find_element(*self.ADD_BUTTON).click()

    def click_cancel_button(self):
        self.find_element(*self.CANCEL_BUTTON).click()
