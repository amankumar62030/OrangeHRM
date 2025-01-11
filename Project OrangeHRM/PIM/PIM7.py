import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(1)

#

username = driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(1)
password = driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(1)
login_button = driver.find_element(By.CLASS_NAME, "oxd-button").click()
time.sleep(1)

# click on PIM
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(1)

#click on Report
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a').click()
time.sleep(1)

try:
    #Report Name
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div/input').send_keys("All Employee Sub Unit Hierarchy Report")
    time.sleep(4)

    # click on search
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(2)
    print("Exist")
except:
    print("Not exist")


driver.close()