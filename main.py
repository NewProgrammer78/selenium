from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)

website = 'https://google.com/'
driver.get(website)
driver.fullscreen_window()

time.sleep(10)


























driver.quit()