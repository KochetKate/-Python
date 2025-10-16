from selenium.webdriver.common.by import By
import allure


class CartPage:
    """
    Page Object класс для работы с корзиной покупок.
    """
    def __init__(self, driver) -> None: 
        """
        Инициализация страницы корзины.

        :param driver: WebDriver - Экземпляр WebDriver
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажать на кнопку оформления заказа")
    def proceed_to_checkout(self) -> None:
        """
        Нажать кнопку оформления заказа.
        :return: None
        """
        self.driver.find_element(*self.checkout_button).click()
