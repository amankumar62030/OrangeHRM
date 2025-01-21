import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# To validate the functionality of "Search" users.
# username
username = driver.find_element(By.NAME,"username").send_keys("Admin")
# password
password = driver.find_element(By.NAME,"password").send_keys("admin123")
# login
driver.find_element(By.CLASS_NAME, "oxd-button").click()
time.sleep(2)

# click on admin
driver.find_element(By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']").click()
time.sleep(1)


# System USers
try:
    user_name = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input")
    user_name.send_keys("Admin")
    time.sleep(2)

    user_role_dropdown = Select(driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]"))
    user_role_dropdown.click()
    time.sleep(2)
    user_role_dropdown.select_by_visible_text("Admin")
    time.sleep(3)

    emp_name = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input")
    emp_name.send_keys("Test Testyan")
    emp_name.send_keys(Keys.DOWN)
    time.sleep(4)

    status_dropdown = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]")
    status_dropdown.click()
    time.sleep(4)
    status_dropdown.send_keys(Keys.DOWN)

    search_button = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    search_button.click()
    time.sleep(6)

    print("Record Found----")
except:
    print("No Record Found---")



driver.quit()