import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.epic("Интернет-магазин")
@pytest.fixture()
def driver():
    """
    Фикстура для инициализации браузера.

    :yields: WebDriver - Экземпляр WebDriver
    """
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.title("Тест оформления заказа")
@allure.description("Полный цикл оформления заказа: авторизация, добавление товаров, оформление")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """
    Тест полного цикла оформления заказа в интернет-магазине.
    """
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_to_cart = ProductsPage(driver)
    products_to_cart.add_product_to_cart("add-to-cart-sauce-labs-backpack")
    products_to_cart.add_product_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    products_to_cart.add_product_to_cart("add-to-cart-sauce-labs-onesie")
    
    products_to_cart.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Екатерина", "Кочетова", "440000")
    
    total_amount = checkout_page.get_total_amount()
    assert total_amount == "58.29", f"Ожидалось $58.29, но получилось ${
        total_amount
    }"
    print(f"✅ Итоговая сумма корректна: ${total_amount}")
