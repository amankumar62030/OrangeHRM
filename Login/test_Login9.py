

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options
from selenium.common.exceptions import NoSuchElementException

class TestClass:
    def test_valid_login(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # print(driver)
        # Enter username
        driver.find_element(By.NAME, "username").send_keys("")
        # Enter password
        driver.find_element(By.NAME, "password").send_keys("")
        # Click login button
        driver.find_element(By.CLASS_NAME, "oxd-button").click()

        # Validate login
        try:
            dashboard_element = driver.find_element(By.LINK_TEXT, "Dashboard")
            assert dashboard_element.is_displayed()
            print("Login Successful")
        except NoSuchElementException:
            pytest.fail("Login Failed")