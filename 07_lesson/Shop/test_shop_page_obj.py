import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_shop(driver):

    # Авторизация
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Добавление товаров в корзину и переход в корзину
    products_to_cart = ProductsPage(driver)
    products_to_cart.add_product_to_cart("add-to-cart-sauce-labs-backpack")
    products_to_cart.add_product_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    products_to_cart.add_product_to_cart("add-to-cart-sauce-labs-onesie")
    products_to_cart.go_to_cart()

    # Нажать на кнопку
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    # Заполнение данных для заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Екатерина", "Кочетова", "440000")
    # Проверка итоговой суммы и сравнение
    total_amount = checkout_page.get_total_amount()
    assert total_amount == "58.29", f"Ожидалось $58.29, но получилось ${
        total_amount
    }"
    print(f"✅ Итоговая сумма корректна: ${total_amount}")
