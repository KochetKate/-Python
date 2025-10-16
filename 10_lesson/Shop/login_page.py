from selenium.webdriver.common.by import By
import allure


class LoginPage:
    """
    Page Object класс для страницы авторизации.
    """
    def __init__(self, driver) -> None:
        """
        Инициализация страницы авторизации.

        driver: WebDriver - Экземпляр WebDriver
        """
        self.driver = driver
        self.driver.maximize_window()
        self.user = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.button = (By.CSS_SELECTOR, "input[type='submit']")

    @allure.step("Выполнить авторизацию")
    def login(self, user_t, password_t) -> None:
        """
        Выполнить авторизацию в системе.

        user_t: str - Логин пользователя
        password_t: str - Пароль пользователя
        Returns: None
        """
        self.driver.find_element(*self.user).send_keys(user_t)
        self.driver.find_element(*self.password).send_keys(password_t)
        self.driver.find_element(*self.button).click()
