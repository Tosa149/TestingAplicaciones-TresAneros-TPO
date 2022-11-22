import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://magento.softwaretestingboard.com/")
link = driver.find_element(By.CLASS_NAME, "authorization-link")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.NAME, "login[username]"))
    )

    element.send_keys("hola@a.com")


    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.NAME, 'login[password]'))
    )

    element.send_keys("Hola1234")


    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'send2'))
    )

    element.click()
    print('Log correcto')

    time.sleep(10)

except TimeoutError:
    print('No encontró el elemento')
    driver.quit()