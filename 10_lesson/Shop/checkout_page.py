from selenium.webdriver.common.by import By
import allure


class CheckoutPage:
    """
    Page Object класс для страницы оформления заказа.
    """
    def __init__(self, driver) -> None:
        """
        Инициализация страницы оформления заказа.

        driver: WebDriver - Экземпляр WebDriver
        """
        self.driver = driver
        # Локаторы для данных
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_cod = (By.ID, "postal-code")
        self.button_continue = (By.ID, "continue")
        self.total = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить форму оформления заказа")
    def fill_checkout_form(self, first, last, code) -> None:
        """
        Заполнить форму данными для доставки.

        first: str - Имя
        last: str - Фамилия  
        code: str - Почтовый индекс
        """
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_cod).send_keys(code)
        self.driver.find_element(*self.button_continue).click()

    @allure.step("Получить итоговую стоимость заказа")
    def get_total_amount(self) -> str:
        """
        Получить итоговую стоимость заказа.
        """
        total_text = self.driver.find_element(*self.total).text
        return total_text.replace("Total: $", "")
