from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    """
    Page Object класс для работы с калькулятором.
    """
    def __init__(self, driver) -> None:
        """
        Инициализация страницы калькулятора.
        
        driver: WebDriver - Экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        # Локаторы элементов
        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")

    @allure.step("Установить задержку калькулятора")
    def set_delay(self, delay_seconds) -> None:
        """
        Установить задержку калькулятора.
        """
        delay_element = self.driver.find_element(*self.delay_field)
        delay_element.clear()
        delay_element.send_keys(str(delay_seconds))

    @allure.step("Нажать кнопку")
    def click_button(self, button_text) -> None:
        """
        Нажать кнопку калькулятора по тексту.
        """
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    @allure.step("Выполнить математическую операцию")
    def perform_calculation(self, num1, operator, num2) -> None:
        """
        Выполнить математическую операцию.

        num1: int | str - Первое число
        operator: str - Оператор
        num2: int | str - Второе число
        """
        self.click_button(str(num1))
        self.click_button(operator)
        self.click_button(str(num2))
        self.click_button("=")

    @allure.step("Ожидать результат вычислений")
    def wait_for_result(self, expected_result, timeout=46) -> None:
        """
        Подождать результат вычислений.

        expected_result: int | str - Ожидаемый результат
        timeout: int - Максимальное время ожидания в секундах
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, str(expected_result))
        )
    @allure.step("Получить результат")
    def get_result(self) -> str:
        """
        Получить текущий результат с экрана.

        Returns: str - Текст результата с экрана калькулятора
        """
        return self.driver.find_element(*self.screen).text
