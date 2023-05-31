from selenium.webdriver.common.by import By
from PageObject.locator import elem
from PageObject.data import data

def test_success_login(driver):
    driver.maximize_window()
    driver.get(data.baseUrl)
    driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(data.correctUser)
    driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(data.correctPass)
    driver.find_element(By.CSS_SELECTOR, elem.loginButton).click()