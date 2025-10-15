# Главная страница с товарами
from selenium.webdriver.common.by import By
import allure


class ProductsPage:
    """
    Page Object класс для страницы с товарами.
    """
    def __init__(self, driver) -> None:
        """
        Инициализация страницы товаров.

        driver: WebDriver - Экземпляр WebDriver
        """
        self.driver = driver

    @allure.step("Добавить товар в корзину")
    def add_product_to_cart(self, product_id) -> None:
        """
        Добавить товар в корзину по ID.

        product_id: str - ID товара
        """
        self.driver.find_element(By.ID, product_id).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Перейти в корзину покупок.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
