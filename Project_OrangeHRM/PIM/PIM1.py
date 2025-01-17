import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(1)

#To Verify "PIM" page loads succesfully.

username = driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(1)
password = driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(1)
login_button = driver.find_element(By.CLASS_NAME,"oxd-button").click()
time.sleep(1)

#click on PIM
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(3)
driver.close()


