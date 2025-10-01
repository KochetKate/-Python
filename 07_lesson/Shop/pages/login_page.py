#Страница авторизации
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        # Локаторы элементов авторизации
        self.user = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.button = (By.CSS_SELECTOR, "input[type='submit']")


    def login(self, user_t, password_t):
        # Выполнить авторизацию
        self.driver.find_element(*self.user).send_keys(user_t)
        self.driver.find_element(*self.password).send_keys(password_t)
        self.driver.find_element(*self.button).click()





