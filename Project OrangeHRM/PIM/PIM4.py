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

# click on add employee
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()
time.sleep(1)

try:
    #upload profile picture
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input').send_keys(r"C:\Users\hi\Downloads\dp.jpg")
    time.sleep(1)

    # First name
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys("Aman")

    #Last name
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys("Kumar")

    # Employee id
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys("2033")

    # create login details
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span').click()
    time.sleep(1)

    # username
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').send_keys("akdhdggd")
    time.sleep(1)

    # password
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').send_keys("Akk#1234")
    time.sleep(1)

    # confirm password
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').send_keys("Akk#1234")
    time.sleep(1)

    # save
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
    time.sleep(4)

    print("Passed-----------")
except:
    print("Failed--------------")

driver.quit()