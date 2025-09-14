from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def make_screenshoot(browser):
    browser.maximize_window() #сделать максимально большое окно
    browser.get("https://ya.ru")
    browser.save_screenshot('./ya_'+browser.name+'.png')
    browser.quit

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

make_screenshoot(chrome)
make_screenshoot(ff)


#browser.back()  вернуться назад
#browser.forward() вернуться вперед
#browser.refresh() обновить страницу
# пкпи
# browser.set_window_size(640, 480) - задать размер экрана (окна)
