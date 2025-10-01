import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalcPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

def test_calculator_addition(driver):
    # Тест сложения чисел с задержкой"""
    # Создаем объект страницы калькулятора
    calculator = CalcPage(driver)
    
    # 1. Устанавливаем задержку 45 секунд
    calculator.set_delay(45)
    
    # 2. Выполняем операцию: 7 + 8 =
    calculator.perform_calculation(7, "+", 8)
    
    # 3. Ждем результат 15 в течение 46 секунд
    calculator.wait_for_result(15, 46)
    
    # 4. Проверяем результат
    result = calculator.get_result()
    assert result == "15", f"Ожидалось 15, но получилось {result}"
    print("✅ Результат 15 отобразился корректно!")