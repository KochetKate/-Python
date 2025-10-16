import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calc_page import CalcPage


@allure.epic("Калькулятор")
@pytest.fixture()
def driver():
    """
    Фикстура для инициализации браузера.

    :yields: WebDriver - Экземпляр WebDriver
    """
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    yield driver
    driver.quit()


@allure.title("Тест сложения чисел с задержкой")
@allure.description("Проверка операции сложения чисел с задержкой в секундах")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_addition(driver):
    """
    Тест сложения чисел с задержкой.
    Проверяет корректность работы калькулятора с установленной задержкой.
    """
    calculator = CalcPage(driver)

    calculator.set_delay(45)
    calculator.perform_calculation(7, "+", 8)
    calculator.wait_for_result(15, 46)
    result = calculator.get_result()

    assert result == "15", f"Ожидалось 15, но получилось {result}"
    print("✅ Результат 15 отобразился корректно!")
