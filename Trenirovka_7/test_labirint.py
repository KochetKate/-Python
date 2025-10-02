from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


cookie = {"name": "cookie_policy", "value": "1"}

def test_card_counter():
   browser = webdriver.Chrome()
  # Перейти на сайт «Лабиринта»
   browser.get("https://www.labirint.ru/")
   browser.implicitly_wait(4)
   browser.maximize_window()
   browser.add_cookie(cookie)
  

  # Найти все книги по слову Python
   browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys("Python")
   browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
   
   # Добавить все книги в корзину и посчитать
   buy_buttons = browser.find_elements(By.CSS_SELECTOR, "[data-carttext]")

   counter = 0
   for btn in buy_buttons:
      btn.click()
      counter += 1

   # Перейти в корзину
   browser.get("https://www.labirint.ru/cart/")
   # Проверить счетчик товаров. Должен быть равен числу нажатий
   # # Получить текущее значение
   txt = browser.find_element(By.ID, 'basket-default-prod-count2').text
   # Сравнить c counter
   assert counter == int(txt.split()[0])

   browser.quit()
