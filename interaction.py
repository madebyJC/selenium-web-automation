from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\\Users\\janns\\PycharmProjects\\chromedriver.exe")
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

# ----------------------------------------------------------------------------------------------------------------------

# EXAMPLES USES

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.fullscreen_window()
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # article_count.click()

# all_portal = driver.find_element(By.LINK_TEXT, "Wikipedia")
# # all_portal.click()

# search_button = driver.find_element(By.NAME, "search")
# search_button.send_keys("Python")
# search_button.send_keys(Keys.ENTER)

# ----------------------------------------------------------------------------------------------------------------------

# https://fill.dev/
# https://fill.dev/form/login-simple

driver.get("https://fill.dev/form/login-simple")
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div/div/div/div[2]/form/div[3]/div/button')

username.send_keys("admin")
password.send_keys("admin123")
password.send_keys(Keys.ENTER)
# OR
# login.click()

sleep(5)

driver.quit()


