from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get("http://uitestingplayground.com/textinput")

button = driver.find_element(By.ID, "newButtonName")
button.clear()
button.send_keys("SkyPro")

driver.find_element(By.ID, "updatingButton").click()
new_button = driver.find_element(By.ID, "updatingButton").text

print(new_button)

driver.quit()
