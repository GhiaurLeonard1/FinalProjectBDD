from selenium.webdriver.common.by import By
from pages.base_page import Basepage

class Sign_In_Page(Basepage):

    EMAIL_INPUT = (By.XPATH, f'//input[@placeholder="Enter your email"]')
    PASS_INPUT = (By.XPATH, f'//input[@placeholder="Enter your password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    FORGOT_PWD = (By.LINK_TEXT, "Forgot password?")


    def navigate_to_sign_in_page(self):
        self.chrome.get("https://jules.app/sign-in")

    def set_mail(self, email):#functie care ne seteaza un email in functie de ce valoare primeste email
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email)#*self.EMAIL_INPUT=(By.XPATH, f'//input[@placeholder="Enter your email"]')

    def set_pass(self, pwd):#functie care ne seteaza un email in functie de ce valoare primeste email
        self.chrome.find_element(*self.PASS_INPUT).send_keys(pwd)

    def click_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def click_forgot_pwd_link(self):
        self.chrome.find_element(*self.FORGOT_PWD).click()

    def check_current_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://jules.app/sign-in"
        self.assertEqual(actual_url, expected_url, "The url does not match")