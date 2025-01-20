# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# time.sleep(2)
# # "To validate the functionality by entering the valid login credentials"
# username = driver.find_element(By.NAME,"username").send_keys("Admin")
# time.sleep(2)
# password = driver.find_element(By.NAME,"password").send_keys("admin123")
# time.sleep(2)
# login_button = driver.find_element(By.CLASS_NAME,"oxd-button").click()
# time.sleep(2)
# try:
#     Dashboard_element = driver.find_element(By.LINK_TEXT,"Dashboard")
#     print("Login Successfull")
# except:
#     print("Login Failed..")
# driver.close()




import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import Options
from selenium.common.exceptions import NoSuchElementException

class TestClass:
    def test_valid_login(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # print(driver)
        # Enter username
        driver.find_element(By.NAME, "username").send_keys("Admin")
        # Enter password
        driver.find_element(By.NAME, "password").send_keys("admin123")
        # Click login button
        driver.find_element(By.CLASS_NAME, "oxd-button").click()

        # Validate login
        try:
            dashboard_element = driver.find_element(By.LINK_TEXT, "Dashboard")
            assert dashboard_element.is_displayed()
            print("Login Successful")
        except NoSuchElementException:
            pytest.fail("Login Failed")