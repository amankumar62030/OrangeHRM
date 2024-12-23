import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# To Verify the redirection to the Reset password page when "Forgot Your Password" is clicked
reset_pass =  driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p").click()
time.sleep(2)

try:
    reset_elements = driver.find_element(By.TAG_NAME,"h6")
    print("Successfully redirected to the reset page")
except:
    print("Failed....")

driver.close()


