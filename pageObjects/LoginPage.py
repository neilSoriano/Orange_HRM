from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXC
from pageObjects.PersonalDetails import PersonalDetails


class LoginPage:
    pimButton = (By.XPATH, "(//li)[2]")
    username = "input[name = 'username']"
    password = "//input[@name='password']"
    loginButton = (By.TAG_NAME, "button")
    header = "h6"

    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)

    def click_pim(self):
        self.driver.find_element(*LoginPage.pimButton).click()
        pim = PersonalDetails(self.driver)
        return pim

    def set_username(self, name):
        self.driver.find_element(By.CSS_SELECTOR, self.username).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.username).send_keys(name)

    def set_password(self, pw):
        self.driver.find_element(By.XPATH, self.password).clear()
        self.driver.find_element(By.XPATH, self.password).send_keys(pw)

    def click_login(self):
        return self.driver.find_element(*LoginPage.loginButton).click()
        
    def get_dashboard_title(self):
        self.WebDriverWait.until(EXC.text_to_be_present_in_element((By.TAG_NAME, self.header), "Dashboard"))
        return self.driver.find_element(By.TAG_NAME, self.header).text
