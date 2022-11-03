import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def user_login(driver, email, wrong_password):
    """
    Correct login to user account

    :param WebDriver driver: instance of webdriver
    :param string email: correct user email
    :param string wrong_password: correct user password
    :return: None
    """
    login_field = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@type="email"]')
    login_field.send_keys(email)
    password_field = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@type="password"]')
    password_field.send_keys(wrong_password, Keys.ENTER)
    time.sleep(1)
