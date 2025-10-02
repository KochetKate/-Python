from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        # Локаторы элементов
        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, delay_seconds):
        # Установить задержку калькулятора
        delay_element = self.driver.find_element(*self.delay_field)
        delay_element.clear()
        delay_element.send_keys(str(delay_seconds))

    def click_button(self, button_text):
        # Нажать кнопку калькулятора по тексту
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    def perform_calculation(self, num1, operator, num2):
        # Выполнить математическую операцию
        self.click_button(str(num1))
        self.click_button(operator)
        self.click_button(str(num2))
        self.click_button("=")

    def wait_for_result(self, expected_result, timeout=46):
        # Подождать результат вычислений
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, str(expected_result))
        )

    def get_result(self):
        # Получить текущий результат с экрана
        return self.driver.find_element(*self.screen).text
