import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# To validate the functionality of adding users to "Job title".
# username
username = driver.find_element(By.NAME,"username").send_keys("Admin")
# password
password = driver.find_element(By.NAME,"password").send_keys("admin123")
# login
driver.find_element(By.CLASS_NAME, "oxd-button").click()
time.sleep(1)

# click on admin
driver.find_element(By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']").click()
time.sleep(1)

# Click on job
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span').click()
time.sleep(1)

# click on pay grade
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]').click()
time.sleep(1)

# click on add
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button').click()
time.sleep(1)

#enter the names
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input').send_keys("Grade 7")
time.sleep(4)

# save
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
time.sleep(4)
driver.quit()