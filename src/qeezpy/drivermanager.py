from selenium import webdriver
import os


class DriverManager:

    def __init__(self):
        self.firefox_profile = webdriver.FirefoxProfile()

    def firefox(self):
        firefox = webdriver.Firefox(
            firefox_profile=self.firefox_profile
        )

        return firefox

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
