from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")
driver.maximize_window() #максимальный размер окна
driver.minimize_window() #минимальный размер окна
driver.fullscreen_window() ##развернуть окно на весь экран (аналог клавиши F11)
driver.set_window_size(1000,600) #задаем размер окна ширина-высота
