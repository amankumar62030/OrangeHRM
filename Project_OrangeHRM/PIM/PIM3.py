import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(1)

# To Verify "PIM" page loads succesfully.

username = driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(1)
password = driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(1)
login_button = driver.find_element(By.CLASS_NAME, "oxd-button").click()
time.sleep(1)

# click on PIM
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(1)

# click on Configuration
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').click()
time.sleep(1)

# click on custom Fields
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]/a').click()
time.sleep(1)

# click on Add
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/button').click()
time.sleep(1)


# Add Custom Field
try:
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input').send_keys("QE")
    time.sleep(1)

    ScreenDrp = Select(driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'))
    ScreenDrp.select_by_visible_text("Personal Details")
    time.sleep(1)

    Typedrp = Select(driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div[1]'))
    Typedrp.select_by_visible_text("Text or Number")
    time.sleep(1)

    # click on save
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
    print("Passed---------")
    time.sleep(4)
except:
    print("Failed......")

driver.close()