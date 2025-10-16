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
        
        :param driver: WebDriver - Экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        # Локаторы элементов
        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")

    @allure.step("Установить задержку калькулятора")
    def set_delay(self, delay_seconds: int) -> None:
        """
        Установить задержку калькулятора.
        :param delay_seconds: количество секунд (int)
        :return: None
        """
        delay_element = self.driver.find_element(*self.delay_field)
        delay_element.clear()
        delay_element.send_keys(str(delay_seconds))

    @allure.step("Нажать кнопку")
    def click_button(self, button_text: str) -> None:
        """
        Нажать кнопку калькулятора по тексту.
        :param button_text: Текст на кнопке (str)
        :return: None
        """
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    @allure.step("Выполнить математическую операцию")
    def perform_calculation(self, num1: int, operator: str, num2: int) -> None:
        """
        Выполнить математическую операцию.
        :param num1: Первое число (int)
        :param operator: Оператор (str)
        :param num2: Второе число (int)
        :return: None
        """
        self.click_button(str(num1))
        self.click_button(operator)
        self.click_button(str(num2))
        self.click_button("=")

    @allure.step("Ожидать результат вычислений")
    def wait_for_result(self, expected_result: str, timeout; int = 46) -> None:
        """
        Подождать результат вычислений.
        :param expected_result: Ожидаемый результат (str)
        :param timeout: Максимальное время ожидания в секундах (int)
        :return: None
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, str(expected_result))
        )

    @allure.step("Получить результат")
    def get_result(self) -> str:
        """
        Получить текущий результат с экрана.
        :return: Текст результата с экрана калькулятора (str)
        """
        return self.driver.find_element(*self.screen).text
