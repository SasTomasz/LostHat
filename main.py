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

    def test_login_page_header(self):
        driver = self.driver
        expected_login_header_text = "Log in to your account"

        driver.get(self.url_login_page)
        login_header = driver.find_element(By.XPATH, '//*[@id="main"]/header[@class="page-header"]/h1')
        self.assertEqual(expected_login_header_text, login_header.text,
                         f"Expected login header text: {expected_login_header_text}, differ from actual: "
                         f"{login_header.text}, for page url: {self.url_login_page}")

    def test_tshirt_card_header(self):
        driver = self.driver
        expected_tshirt_header_text = "HUMMINGBIRD PRINTED T-SHIRT"

        driver.get(self.url_tshirt_cart)
        card_header = driver.find_element(By.XPATH, '//*[@id="main"]//*[@itemprop="name"]')
        self.assertEqual(expected_tshirt_header_text, card_header.text,
                         f"Expected card header text: {expected_tshirt_header_text}, differ from actual: "
                         f"{card_header.text}, for page url: {self.url_tshirt_cart}")

    def test_correct_login(self):
        driver = self.driver
        password = 'RbjHi4wxVeHbbE2'
        login = 'boss7@op.pl'
        expected_user_name = 'Tomasz Sas'

        driver.get(self.url_login_page)

        login_field = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@type="email"]')
        login_field.send_keys(login)

        password_field = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@type="password"]')
        password_field.send_keys(password, Keys.ENTER)
        time.sleep(1)

        desktop_user_name = driver.find_element(By.XPATH, '//*[@id="_desktop_user_info"]//*[@class="hidden-sm-down"]')
        self.assertEqual(expected_user_name, desktop_user_name.text,
                         f"Expected user name: {expected_user_name}, differ from actual: "
                         f"{desktop_user_name.text}, for page url: {self.url_login_page}")

        sign_out_button = driver.find_elements(By.XPATH, '//*[@href="https://autodemo.testoneo.com/en/?mylogout="]')
        sign_out_button[0].click()

    def test_tshirt_card_price(self):
        driver = self.driver
        expected_price = 'PLN23.52'

        driver.get(self.url_tshirt_cart)
        card_price = driver.find_element(By.XPATH, '//*[@id="main"]//*[@itemprop="price"]')
        self.assertEqual(expected_price, card_price.text, f"Expected card price: {expected_price}, differ from actual: "
                                                          f"{card_price.text}, for page url {self.url_tshirt_cart}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
