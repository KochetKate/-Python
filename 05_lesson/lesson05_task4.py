from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

login = driver.find_element(By.ID, "username")
login.send_keys("tomsmith")

passw = driver.find_element(By.ID, "password")
passw.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in").click()

final = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(final.text)

driver.quit()
