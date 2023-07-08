from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXC


class PersonalDetails:
    header = "h6"
    addEmployee = (By.CSS_SELECTOR, "i.oxd-icon.bi-plus.oxd-button-icon")
    firstName = "firstName"
    middleName = "middleName"
    lastName = "lastName"
    saveButton = (By.CSS_SELECTOR, "button[type='submit']")
    pdPage = "//h6[text()='Personal Details']"

    licenseNumber = "(//input[@class='oxd-input oxd-input--active'])[5]"
    licenseExpiry = "(//input[@class='oxd-input oxd-input--active'])[6]"
    ssn = "(//input[@class='oxd-input oxd-input--active'])[7]"
    nationality = "(//div[@class='oxd-select-text-input'])[1]"
    maritalStatus = "(//div[@class='oxd-select-text-input'])[2]"
    dob = "(//input[@placeholder='yyyy-mm-dd'])[2]"
    genderTitle = "//label[text()='Gender']"
    # gender locator is 2 elements
    gender = ".oxd-radio-input.oxd-radio-input--active.--label-right.oxd-radio-input"
    bloodType = "(//div[@class='oxd-select-text oxd-select-text--active'])[3]"
    opType = "//div[.='O+']"
    customFieldsTitle = "//h6[text()='Custom Fields']"

    pdSave = "(//button[@type='submit'])[1]"
    customSave = "(//button[@type='submit'])[2]"

    updatedMsg = "//p[text() = 'Successfully Updated']"
    savedMsg = "//p[text() = 'Successfully Saved']"

    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)

    def add_employee(self):
        return self.driver.find_element(*PersonalDetails.addEmployee).click()

    def set_first_name(self, name):
        self.driver.find_element(By.NAME, self.firstName).clear()
        self.driver.find_element(By.NAME, self.firstName).send_keys(name)

    def set_middle_name(self, name):
        self.driver.find_element(By.NAME, self.middleName).clear()
        self.driver.find_element(By.NAME, self.middleName).send_keys(name)

    def set_last_name(self, name):
        self.driver.find_element(By.NAME, self.lastName).clear()
        self.driver.find_element(By.NAME, self.lastName).send_keys(name)

    def wait_for_title_load(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EXC.presence_of_element_located((By.XPATH, self.pdPage)))

    def wait_for_custom_load(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EXC.presence_of_element_located((By.XPATH, self.customFieldsTitle)))

    def set_driver_license(self, number):
        self.driver.find_element(By.XPATH, self.licenseNumber).clear()
        self.driver.find_element(By.XPATH, self.licenseNumber).send_keys(number)

    def set_license_expiry(self, date):
        self.driver.find_element(By.XPATH, self.licenseExpiry).clear()
        self.driver.find_element(By.XPATH, self.licenseExpiry).send_keys(date)

    def set_ssn(self, number):
        self.driver.find_element(By.XPATH, self.ssn).clear()
        self.driver.find_element(By.XPATH, self.ssn).send_keys(number)

    def set_nationality(self, nationality):
        self.driver.find_element(By.XPATH, self.nationality).click()
        self.driver.find_element(By.XPATH, self.nationality).send_keys(nationality)

    def set_marital_status(self, status):
        self.driver.find_element(By.XPATH, self.maritalStatus).click()
        self.driver.find_element(By.XPATH, self.maritalStatus).send_keys(status)

    def set_dob(self, date):
        self.driver.find_element(By.XPATH, self.dob).click()
        self.driver.find_element(By.XPATH, self.dob).send_keys(date)

    def set_gender(self, gender):
        self.driver.find_element(By.XPATH, self.genderTitle).click()
        genders = self.driver.find_elements(By.CSS_SELECTOR, self.gender)
        if gender == "Male":
            genders[0].click()
        elif gender == "Female":
            genders[1].click()
        else:
            genders[0].click()

    def save_new_details(self):
        return self.driver.find_element(By.XPATH, self.pdSave).click()

    def set_blood_type(self):
        self.driver.find_element(By.XPATH, self.bloodType).click()
        self.driver.find_element(By.XPATH, self.opType).click()

    def save_blood_type(self):
        return self.driver.find_element(By.XPATH, self.customSave).click()

    def save_new_employee(self):
        return self.driver.find_element(*PersonalDetails.saveButton).click()

    def get_title(self):
        self.WebDriverWait.until(EXC.text_to_be_present_in_element((By.XPATH, self.pdPage), "Personal Details"))
        return self.driver.find_element(By.XPATH, self.pdPage).text

    def get_success_update(self):
        self.WebDriverWait.until(EXC.text_to_be_present_in_element((By.XPATH, self.updatedMsg), "Successfully Updated"))
        return self.driver.find_element(By.XPATH, self.updatedMsg).text

    def get_success_save(self):
        self.WebDriverWait.until(EXC.text_to_be_present_in_element((By.XPATH, self.savedMsg), "Successfully Saved"))
        return self.driver.find_element(By.XPATH, self.savedMsg).text
