from selenium import webdriver
import os


class FirefoxDriver:

    def __init__(self):
        self.firefox_profile = webdriver.FirefoxProfile()
        self.driver = webdriver.Firefox(
            firefox_profile=self.firefox_profile
        )

    def set_firefox_profile(self):
        """
        This function is to create firefox profile.
        :return: firefox profile.
        """
        self.firefox_profile.set_preference('browser.download.folderList', 2)  # custom location
        self.firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
        self.firefox_profile.set_preference('browser.download.dir', os.getcwd())
        self.firefox_profile.set_preference(
            'browser.helperApps.neverAsk.saveToDisk',
            'text/csv,application/octet-stream,application/pdf,application/vnd.ms-excel'
        )
        self.firefox_profile.set_preference("pdfjs.disabled", True)

    def return_driver(self):
        return self.driver
