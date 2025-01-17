import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# To Verify the presence of the "Forgot Your Password" link

try:
    link_texts = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")
    time.sleep(2)
    print("Yes,the link is present on login page.")
except:
    print("NO,the link is not present on login page.")

driver.close()


