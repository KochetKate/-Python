from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.saucedemo.com/")

# Пройти авторизацию
user = driver.find_element(By.ID, "user-name")
user.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

# Нажать на кнопку
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

# Добавление товаров в корзину
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

# Перейти в корзину
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Нажать на кнопку
driver.find_element(By.ID, "checkout").click()

# Ввести данные для отправки товаров
first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Екатерина")

last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Кочетова")

postal = driver.find_element(By.ID, "postal-code")
postal.send_keys("440000")

# Нажать на кнопку
driver.find_element(By.ID, "continue").click()

# Прочитать итоговую стоимость
total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
total_text = total_element.text
total_amount = total_text.replace("Total: $", "")

# Проверить что итоговая сумма равна $58.29
assert total_amount == "58.29", f"Ожидалось $58.29, но получилось ${total_amount}"
print(f"Итоговая сумма корректна: ${total_amount}")

driver.quit()
