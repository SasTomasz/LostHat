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

    def test_correct_login(self):
        driver = self.driver
        correct_password = 'RbjHi4wxVeHbbE2'
        correct_login = 'boss7@op.pl'
        expected_user_name = 'Tomasz Sas'
        url = self.url_login_page

        driver.get(url)

        login_field = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@type="email"]')
        login_field.send_keys(correct_login)

        password_field = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@type="password"]')
        password_field.send_keys(correct_password, Keys.ENTER)
        time.sleep(1)

        desktop_user_name = driver.find_element(By.XPATH, '//*[@id="_desktop_user_info"]//*[@class="hidden-sm-down"]')
        self.assertEqual(expected_user_name, desktop_user_name.text,
                         f"Expected user name: {expected_user_name}, differ from actual: "
                         f"{desktop_user_name.text}, for page url: {self.url_login_page}")

        sign_out_button = driver.find_elements(By.XPATH, '//*[@href="https://autodemo.testoneo.com/en/?mylogout="]')
        sign_out_button[0].click()

    def test_fail_login(self):
        driver = self.driver
        wrong_password = 'wrong_P@SS'
        wrong_login = 'biss7@o2.pl'
        expected_alert_dialog_text = 'Authentication failed.'
        url = self.url_login_page

        driver.get(url)

        login_field = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@type="email"]')
        login_field.send_keys(wrong_login)

        password_field = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@type="password"]')
        password_field.send_keys(wrong_password, Keys.ENTER)
        time.sleep(1)

        alert_dialog = driver.find_element(By.XPATH, '//*[@id="content"]//*[@class="alert alert-danger"]')
        self.assertEqual(expected_alert_dialog_text, alert_dialog.text,
                         f"Expected alert dialog text: {expected_alert_dialog_text}, differ from actual: "
                         f"{alert_dialog.text}, for page url: {url}")

    def test_login_page_header(self):
        driver = self.driver
        expected_login_header_text = "Log in to your account"
        url = self.url_login_page

        driver.get(url)
        login_header = driver.find_element(By.XPATH, '//*[@id="main"]/header[@class="page-header"]/h1')
        self.assertEqual(expected_login_header_text, login_header.text,
                         f"Expected login header text: {expected_login_header_text}, differ from actual: "
                         f"{login_header.text}, for page url: {url}")

    def test_tshirt_card_header(self):
        driver = self.driver
        expected_tshirt_header_text = "HUMMINGBIRD PRINTED T-SHIRT"
        url = self.url_tshirt_cart

        driver.get(url)
        card_header = driver.find_element(By.XPATH, '//*[@id="main"]//*[@itemprop="name"]')
        self.assertEqual(expected_tshirt_header_text, card_header.text,
                         f"Expected card header text: {expected_tshirt_header_text}, differ from actual: "
                         f"{card_header.text}, for page url: {url}")

    def test_tshirt_card_price(self):
        driver = self.driver
        expected_price = 'PLN23.52'
        url = self.url_tshirt_cart

        driver.get(url)
        card_price = driver.find_element(By.XPATH, '//*[@id="main"]//*[@itemprop="price"]')
        self.assertEqual(expected_price, card_price.text, f"Expected card price: {expected_price}, differ from actual: "
                                                          f"{card_price.text}, for page url {url}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
