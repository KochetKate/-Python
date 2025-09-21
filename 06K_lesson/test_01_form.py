from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = r"C:\Users\User\Desktop\документы катя\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
first_name.send_keys("Иван")

last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
last_name.send_keys("Петров")

addres = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
addres.send_keys("Ленина, 55-3")

email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
email.send_keys("test@skypro.com")

phone = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
phone.send_keys("+7985899998787")

z_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
z_code.clear()

city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
city.send_keys("Москва")

country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
country.send_keys("Россия")

job = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
job.send_keys("QA")

company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
company.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
)

zip_code_field = driver.find_element(By.ID, "zip-code")
assert "alert-danger" in zip_code_field.get_attribute("class"), "Zip code не красный"

green_fields = [
    "first-name",
    "last-name",
    "address",
    "e-mail",
    "phone",
    "city",
    "country",
    "job-position",
    "company"
]

for selector in green_fields:
    field = driver.find_element(By.ID, selector)
    assert "alert-success" in field.get_attribute("class"), f"Поле {selector} не зеленое"

print("Все проверки выполнены успешно")

driver.quit()
