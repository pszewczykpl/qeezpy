from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from resources.data import *


class Driver(object):
    def __init__(self):
        self.firefox_profile = webdriver.FirefoxProfile()
        self.firefox_profile.set_preference("browser.download.folderList", 2)
        self.firefox_profile.set_preference("browser.download.dir",
                                            'C:\\Users\\pszewczyk\\Desktop\\Projects\\Tests Docs')
        self.firefox_profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
        self.firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                            "application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream")
        self.firefox_profile.set_preference("browser.download.manager.showWhenStarting", False)
        self.firefox_profile.set_preference("browser.download.manager.focusWhenStarting", False)
        self.firefox_profile.set_preference("browser.download.useDownloadDir", True)
        self.firefox_profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        self.firefox_profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
        self.firefox_profile.set_preference("browser.download.manager.closeWhenDone", True)
        self.firefox_profile.set_preference("browser.download.manager.showAlertOnComplete", False)
        self.firefox_profile.set_preference("browser.download.manager.useWindow", False)
        self.firefox_profile.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
        self.firefox_profile.set_preference("pdfjs.disabled", True)

        self.driver = webdriver.Firefox(firefox_profile=self.firefox_profile)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.get(LoginPageData.BASE_URL)
