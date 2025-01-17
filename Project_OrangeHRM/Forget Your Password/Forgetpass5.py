import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# To Verify password reset functionality with blank username
reset_pass =  driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p").click()
time.sleep(2)

username = driver.find_element(By.NAME,"username").send_keys("")
time.sleep(2)

reset_pass = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]").click()
time.sleep(2)

try:
    reset_elements = driver.find_element(By.XPATH,"//span[text()]")
    print("Pass---------")
except:
    print("Fail-------")

driver.close()
