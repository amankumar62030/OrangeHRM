import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# To validate the functionality of "Search" users.
# username
username = driver.find_element(By.NAME,"username").send_keys("Admin")
# password
password = driver.find_element(By.NAME,"password").send_keys("admin123")
# login
driver.find_element(By.CLASS_NAME, "oxd-button").click()
time.sleep(2)

# click on admin
driver.find_element(By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']").click()
time.sleep(1)


try:
    delete_button = driver.find_element(By.XPATH, "//div[@role='rowgroup']//div[2]//div[1]//div[6]//div[1]//button[1]//i[1]")
    delete_button.click()
    time.sleep(2)
    confirm_delete_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')  # Fixed locator
    confirm_delete_button.click()
    time.sleep(2)
    print("User Deleted Successfully")
except Exception as e:
    print("Failed to delete user:", str(e))


driver.quit()