Проект автоматизации тестирования
На данном уроке рассматривали два проекта для автоматизации тестирования веб-приложений с использованием Selenium WebDriver, Pytest и Allure.

Структура урока №10
Calculator/ - Тестирование калькулятора с задержкой выполнения операций
Shop/ - Тестирование интернет-магазина (полный цикл оформления заказа)

Calculator - Автоматизация тестирования калькулятора с задержкой выполнения операций.
Структура проекта:
Calculator/
├── calc_page.py
└── test_calc_page_obj.py

Назначение файлов:
- calc_page.py - содержит класс CalcPage с методами для взаимодействия с элементами калькулятора
- test_calc_page_obj.py - тестовые сценарии для проверки операций калькулятора
Запуск тестов:
1. Перейдите в папку проекта:
cd Calculator
2. Установите зависимости:
pip install -r requirements.txt
3. Запустите тесты с генерацией Allure-отчетов:
pytest test_calc_page_obj.py --alluredir=allure-results -v
4. Просмотр отчета
allure serve allure-results

Shop - Автоматизация тестирования интернет-магазина (полный цикл оформления заказа).
Структура проекта:
Shop/
├── login_page.py
├── products_page.py
├── cart_page.py
├── checkout_page.py
└── test_shop_page_obj.py
Назначение файлов:
- login_page.py - класс LoginPage для авторизации в системе
- products_page.py - класс ProductsPage для работы с товарами
- cart_page.py - класс CartPage для управления корзиной
- checkout_page.py - класс CheckoutPage для оформления заказа
- test_shop_page_obj.py - основной тест, проверяющий полный цикл покупки
Запуск тестов:
1. Перейдите в папку проекта:
cd Shop
2. Установите зависимости:
pip install -r requirements.txt
3. Запустите тесты с генерацией Allure-отчетов:
pytest test_shop.py --alluredir=allure-results -v
4. Просмотр отчета
allure serve allure-results


Зависимости
Основные зависимости для обоих проектов:
pytest==8.4.2
selenium==4.35.0
webdriver-manager==4.0.1
allure-pytest==2.13.2

Важные примечания
- Убедитесь, что у вас установлен Java для работы с Allure
- Для каждого запуска рекомендуется очищать папку allure-results перед генерацией новых отчетов
- Папки allure-results и allure-report не коммитить в репозиторий

Дополнительные команды
* Очистка предыдущих результатов
rm -rf allure-results
* Запуск всех тестов в проекте
pytest --alluredir=allure-results -v
* Генерация статического отчета
allure generate allure-results -o allure-report
-После генерации статического отчета можно открыть файл allure-report/index.html в браузере.

Все тесты используют паттерн Page Object Model (POM) для улучшения поддерживаемости кода и включают полную документацию методов с указанием типов параметров и возвращаемых значений.