import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


class LostHatTests(unittest.TestCase):
    url_base = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service('C://TestFiles/chromedriver.exe'))

        cls.url_base = 'https://autodemo.testoneo.com/en/'
        cls.url_login_page = cls.url_base + 'login?back=my-account'
        cls.url_tshirt_cart = cls.url_base + 'men/1-1-hummingbird-printed-t-shirt.html'

    def assert_element_text(self, driver, xpath, expected_text):
        element = driver.find_element(By.XPATH, xpath)
        self.assertEqual(expected_text, element.text, f"Expected element text: {expected_text}, differ from actual: "
                                                      f"{element.text}, for page url: {driver.current_url}")

    def test_correct_login(self):
        driver = self.driver
        correct_password = 'RbjHi4wxVeHbbE2'
        correct_login = 'boss7@op.pl'
        expected_user_name = 'Tomasz Sas'
        xpath_user_name = '//*[@id="_desktop_user_info"]//*[@class="hidden-sm-down"]'
        url = self.url_login_page

        driver.get(url)

        self.user_login(driver, correct_login, correct_password)
        self.assert_element_text(driver, xpath_user_name,
                                 expected_user_name)

        sign_out_button = driver.find_elements(By.XPATH, '//*[@href="https://autodemo.testoneo.com/en/?mylogout="]')
        sign_out_button[0].click()

    def test_fail_login(self):
        driver = self.driver
        wrong_password = 'wrong_P@SS'
        wrong_login = 'biss7@o2.pl'
        expected_alert_dialog_text = 'Authentication failed.'
        xpath_dialog_alert = '//*[@id="content"]//*[@class="alert alert-danger"]'
        url = self.url_login_page

        driver.get(url)

        self.user_login(driver, wrong_login, wrong_password)
        self.assert_element_text(driver, xpath_dialog_alert,
                                 expected_alert_dialog_text)

    @staticmethod
    def user_login(driver, login, wrong_password):
        login_field = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@type="email"]')
        login_field.send_keys(login)
        password_field = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@type="password"]')
        password_field.send_keys(wrong_password, Keys.ENTER)
        time.sleep(1)

    def test_login_page_header(self):
        driver = self.driver
        expected_login_header_text = "Log in to your account"
        xpath_login_header = '//*[@id="main"]/header[@class="page-header"]/h1'
        url = self.url_login_page

        driver.get(url)
        self.assert_element_text(driver, xpath_login_header, expected_login_header_text)

    def test_tshirt_card_header(self):
        driver = self.driver
        expected_tshirt_header_text = "HUMMINGBIRD PRINTED T-SHIRT"
        xpath_tshirt_header = '//*[@id="main"]//*[@itemprop="name"]'
        url = self.url_tshirt_cart

        driver.get(url)
        self.assert_element_text(driver, xpath_tshirt_header, expected_tshirt_header_text)

    def test_tshirt_card_price(self):
        driver = self.driver
        expected_price = 'PLN23.52'
        xpath_price = '//*[@id="main"]//*[@itemprop="price"]'
        url = self.url_tshirt_cart

        driver.get(url)
        self.assert_element_text(driver, xpath_price, expected_price)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
