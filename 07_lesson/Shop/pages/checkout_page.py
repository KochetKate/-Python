# Страница оформления заказа
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        # Локаторы для данных
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_cod = (By.ID, "postal-code")
        self.button_continue = (By.ID, "continue")
        self.total = (By.CLASS_NAME, "summary_total_label")


    def fill_checkout_form(self, first, last, code):
        # Внести данные для отправки товаров и нажать на кнопку "Продолжить"
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_cod).send_keys(code)
        self.driver.find_element(*self.button_continue).click()


    def get_total_amount(self):
        # Прочитать итоговую стоимость
       total_text = self.driver.find_element(*self.total).text
       return total_text.replace("Total: $", "")

