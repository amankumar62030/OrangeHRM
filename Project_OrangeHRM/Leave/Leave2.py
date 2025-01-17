import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# To Verify "Leave" page loads succesfully.

username = driver.find_element(By.NAME,"username")
username.send_keys("Admin")
password = driver.find_element(By.NAME,"password")
password.send_keys("admin123")
driver.find_element(By.CLASS_NAME, "oxd-button").click()
time.sleep(1)

# click on Leave
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()
time.sleep(1)


date = "2"
month = "January"
Year = "2025"

# from date
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').click()
time.sleep(2)

while True:
    mo = driver.find_elements(By.XPATH,'')


driver.close()


