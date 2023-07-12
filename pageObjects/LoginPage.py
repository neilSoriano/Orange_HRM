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
    arrow = ".oxd-icon.bi-caret-down-fill.oxd-userdropdown-icon"
    logout_button = "(//a[contains(@class,'oxd-userdropdown-link')])[4]"
    invalid_login = ".oxd-text.oxd-text--p.oxd-alert-content-text"

    book_path = "/Users/neilsoriano/PycharmProjects1/pythonTesting/OrangeHRM_Demo/TestData/LoginPageData.xlsx"
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

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

    def log_out(self):
        self.WebDriverWait.until((EXC.presence_of_element_located((By.CSS_SELECTOR, self.arrow))))
        self.driver.find_element(By.CSS_SELECTOR, self.arrow).click()
        self.WebDriverWait.until(EXC.presence_of_element_located((By.XPATH, self.logout_button)))
        return self.driver.find_element(By.XPATH, self.logout_button).click()

    def get_invalid_text(self):
        self.WebDriverWait.until((EXC.presence_of_element_located((By.CSS_SELECTOR, self.invalid_login))))
        return self.driver.find_element(By.CSS_SELECTOR, self.invalid_login).text
