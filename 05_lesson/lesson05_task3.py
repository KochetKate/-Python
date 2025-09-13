from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/inputs")

s_input = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
s_input.send_keys("Sky")
s_input.clear()
s_input.send_keys("Pro")
driver.quit()
