from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    chrome.implicitly_wait(10)
    chrome.set_page_load_timeout(10)
    chrome.maximize_window()

    def close(self):
        self.chrome.close()










#install-uri
#pip install selenium
# pip install behave
# (pentru java e cucumber)
# pip install behave-html-formatter
# pip install webdriver-manager
from browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest