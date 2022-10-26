from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class LoginPageTests(unittest.TestCase):
    driver = None
    login_page_url = 'https://autodemo.testoneo.com/en/login?back=my-account'

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service('C://TestFiles/chromedriver.exe'))

    def test_login_page_header(self):
        driver = self.driver
        driver.get(self.login_page_url)
        login_header = driver.find_element(By.XPATH, '//*[@id="main"]/header[@class="page-header"]/h1')
        self.assertEqual("Log in to your account", login_header.text,
                         f"Expected login header text: 'Log in to your account, differ from actual: "
                         f"{login_header.text}, for page url: {self.login_page_url}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
