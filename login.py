from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.set_window_size(1120, 550)
#driver.manage().wndow.maximize()
driver.implicitly_wait(50)
wait = WebDriverWait(driver, 20)

print("Loading login page...")
driver.get("https://accounts.google.com/ServiceLogin?service=mail#identifier")
driver.set_window_size(1000, 800);
usernametext = driver.find_element_by_name('Email')
usernametext.send_keys('')
driver.find_element_by_name('signIn').click()
passwordtext = driver.find_element_by_name('Passwd') \
                      .send_keys(['', Keys.RETURN])
print("Signed in. Going to sleep...")

#Time to sleep a little
time.sleep(23)
print("Waking up. Going to compose message...")

#Find the compose button
driver.find_element_by_xpath("//div[contains(text(),'COMPOSE')]").click();


driver.close()

