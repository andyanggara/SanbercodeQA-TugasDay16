import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import baseLogin
from PageObject.locator import elem
from PageObject.data import data

class TestLogin(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)

    #   Test Case 1: Successful login with correct username and password
    def test_success_login(self):
        driver = self.browser
        baseLogin.test_success_login(driver)

        #   Assert app logo
        appLogo = driver.find_element(By.CLASS_NAME, elem.appLogo).text
        self.assertEqual("Swag Labs", appLogo)

        driver.find_element(By.ID, elem.hamburgerMenu).click()
        sleep(1)

        #   Assert logout button
        logoutButton = driver.find_element(By.ID, elem.logoutButton).text
        self.assertEqual("Logout", logoutButton)

        #   Assert current url
        currentUrl = driver.current_url
        self.assertIn("/inventory.html", currentUrl)

    #   Test Case 2: Failed login with blank username and blank password
    def test_blank_username_password(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(data.baseUrl)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys("")
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys("")
        driver.find_element(By.CSS_SELECTOR, elem.loginButton).click()

        #   Assert error message
        errorMessage = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertEqual(data.emptyUser, errorMessage)

    #   Test Case 3: Failed login with blank username
    def test_blank_username(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(data.baseUrl)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys("")
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys("")
        driver.find_element(By.CSS_SELECTOR, elem.loginButton).click()

        #   Assert error message
        errorMessage = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertEqual(data.emptyUser, errorMessage)

    #   Test Case 4: Failed login with blank password
    def test_blank_password(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(data.baseUrl)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(data.correctUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys("")
        driver.find_element(By.CSS_SELECTOR, elem.loginButton).click()

        #   Assert error message
        errorMessage = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertEqual(data.emptyPass, errorMessage)

    #   Test Case 5: Failed login with incorrect username
    def test_incorrect_username(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(data.baseUrl)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(data.wrongUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(data.correctPass)
        driver.find_element(By.CSS_SELECTOR, elem.loginButton).click()

        #   Assert error message
        errorMessage = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertEqual(data.notMatch, errorMessage)
    
    #   Test Case 6: Failed login with incorrect password
    def test_incorrect_password(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(data.baseUrl)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(data.correctUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(data.wrongPass)
        driver.find_element(By.CSS_SELECTOR, elem.loginButton).click()

        #   Assert error message
        errorMessage = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertEqual(data.notMatch, errorMessage)
    
    #   Test Case 7: Failed login with locked user
    def test_locked_user(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(data.baseUrl)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(data.lockedUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(data.correctPass)
        driver.find_element(By.CSS_SELECTOR, elem.loginButton).click()

        #   Assert error message
        errorMessage = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertEqual(data.lockUser, errorMessage)

    def tearDown(self):
        sleep(1)
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
