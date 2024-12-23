import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# To Verify "Admin" page loads succesfully.

username = driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(2)
password = driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "oxd-button").click()
time.sleep(2)

driver.find_element(By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']").click()
time.sleep(5)

try:
    admin_page = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]")
    print("Admin page loaded sucessfully")
except:
    print("Admin Page load failed..")

driver.close()


