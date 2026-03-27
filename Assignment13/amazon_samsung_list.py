from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

driver.maximize_window()
time.sleep(1)

search = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("samsung")

driver.find_element(By.ID, "nav-search-submit-button").click()

list = driver.find_elements(By.XPATH, "//h2[contains(@aria-label, 'Galaxy')]")

print(str(len(list)) + ' products found')

for i in list:
    print(i.text)

driver.quit()