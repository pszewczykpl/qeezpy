from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.page import Page


class RegionPage(Page):
    ##
    # SZUKAJ MAKROREGIONU/REGIONU
    ##
    REGION_NAME_INPUT = (By.ID, 'name')
    REGION_SYMBOL_INPUT = (By.ID, 'symbol')
