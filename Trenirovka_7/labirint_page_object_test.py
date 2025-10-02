from selenium import webdriver
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage

def test_cart_counter():
	browser = webdriver.Chrome()  # Открываем браузер
	main_page = MainPage(browser)  # Экземпляр класса с передачей драйвера
	main_page.set_cookie_policy()  # Вызываем метод
	result_page = ResultPage(browser)
	result_page.add_books()
	to_be = result_page.add_books()  # Результат вызова add_books
	cart_page = CartPage(browser)
	cart_page.get()  # Переход на страницу с корзиной
	as_is = cart_page.get_counter()  # Текущее значение счетчика на странице 
	assert as_is == to_be