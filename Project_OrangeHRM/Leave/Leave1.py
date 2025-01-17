import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(1)
act=ActionChains(driver)

# To Verify "PIM" page loads succesfully.

driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(1)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "oxd-button").click()
time.sleep(4)

# click on PIM
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(2)

# click on Configuration
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').click()
time.sleep(2)

# click on custom Fields
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]/a').click()
time.sleep(2)

# click on Add
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/button').click()
time.sleep(2)


# Add Custom Field
try:
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input').send_keys("QE")
    time.sleep(2)

    screen=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div')
    screen.click()
    time.sleep(3)
    act.key_down(Keys.DOWN).key_up(Keys.DOWN).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()

    typedrp = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div[1]')
    typedrp.click()
    time.sleep(3)
    act.key_down(Keys.DOWN).key_up(Keys.DOWN).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
    time.sleep(2)


    # click on save
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
    print("Passed---------")
    time.sleep(4)
except:
    print("Failed......")

driver.close()