import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.PersonalDetails import PersonalDetails
from utilities.BaseClass import BaseClass


class TestAddEmployee(BaseClass):

    @pytest.mark.sanity
    def test_add_employee(self):
        log = self.get_logger()

        log.info("Test for adding a new employee to the HR system")

        log.info("Starting log in")
        login = LoginPage(self.driver)
        login.set_username(self.username)
        login.set_password(self.password)
        login.click_login()
        log.info("Logged in")

        pim = login.click_pim()
        log.info("On PIM page now")
        pim.add_employee()
        log.info("Reached to add employee page")

        pim.set_first_name("Monkey")
        pim.set_middle_name("D.")
        pim.set_last_name("Luffy")
        pim.save_new_employee()

        log.info("New employee added")

        pageTitle = pim.get_title()

        assert "Personal Details" in pageTitle
        log.info("Assertion passes")

    @pytest.mark.sanity
    def test_add_details(self):
        log = self.get_logger()

        log.info("Adding new employee details")
        pd = PersonalDetails(self.driver)
        pd.wait_for_title_load()
        pd.set_driver_license("L47582")
        pd.set_license_expiry("2026-05-13")
        pd.set_ssn("3527320")
        pd.set_nationality("c")
        pd.set_marital_status("s")
        pd.set_dob("1995-04-28")
        self.scroll_to_bottom()
        pd.set_gender("Male")
        # self.scroll_to_bottom()
        pd.save_new_details()

        log.info("Updating new personal details")
        updatedMsg = pd.get_success_update()

        if updatedMsg == "Successfully Updated":
            log.info("Successfully updated personal details")
            assert True
        else:
            log.error("Successfully Updated message did not match or appear")
            assert False
        pd.wait_for_custom_load()

        log.info("Adding blood type")
        pd.set_blood_type()
        pd.save_blood_type()
        log.info("Saving blood type")
        savedMsg = pd.get_success_save()

        if savedMsg == "Successfully Saved":
            log.info("Successfully Saved blood type")
            assert True
        else:
            log.error("Successfully Saved message did not match or appear")
            assert False







