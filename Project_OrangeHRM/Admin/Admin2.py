import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# To validate the functionality of "Add" users.
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

# click on add
driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
time.sleep(2)

# elements
user_role_dropdown = driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input']")
user_role_dropdown.click()
time.sleep(2)
user_role_dropdown.send_keys(Keys.DOWN)


emp_name = driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']")
emp_name.send_keys("A")
emp_name.send_keys(Keys.DOWN)
time.sleep(3)

status_dropdown = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]")
status_dropdown.click()
time.sleep(3)
status_dropdown.send_keys(Keys.DOWN)
time.sleep(2)

user_name = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input")
user_name.send_keys("new_users")
time.sleep(2)

pass_word = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input")
pass_word.send_keys("NewUser@123")

confirm_pass = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input")
confirm_pass.send_keys("NewUser@123")

save_button = driver.find_element(By.XPATH, '//button[contains(@type, "submit")]')
save_button.click()
time.sleep(5)

print("User added successfully")

driver.quit()


