from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://labirint.ru/")

my_cookie = {
    'name' : 'cookie_policy',
    'value' : '1'
}

driver.add_cookie(my_cookie)  #добавить куки 
cookies = driver.get_cookies() #просмотр всех куки
print(cookies)
driver.refresh() #обновить

# driver.delete_all_cookies()
# driver.refresh() #обновить
sleep(5)
driver.quit()