import pytest

from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):

    @pytest.mark.regression
    def test_page_title(self):
        log = self.get_logger()
        log.info("Page Title Test")

        LoginPage(self.driver)

        act_title = self.driver.title
        if act_title == "OrangeHRM":
            log.info("Page Title Test PASS")
            assert True
        else:
            log.error("Page Title Test FAIL")
            # add screenshot for failed case
            self.driver.get_screenshot_as_file("../Screenshots/test_page_title.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self):
        log = self.get_logger()
        login = LoginPage(self.driver)

        log.info("Entering username...")
        login.set_username(self.username)

        log.info("Entering password...")
        login.set_password(self.password)

        login.click_login()
        # confirm landing on Dashboard page
        dashboard_title = login.get_dashboard_title()

        assert "Dashboard" in dashboard_title




