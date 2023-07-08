import inspect
import logging

import pytest

# use useFixtures("setup") to use fixture method from conftest
from TestData.LoginPageData import LoginPageData
from utilities.readProperties import ReadConfig


# if there are any common utilities you think will be used multiple times,
# add to BaseClass since all functions it will be available to the test file

@pytest.mark.usefixtures("setup")
class BaseClass:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def get_logger(self):
        # inspect.stack() returns the nested list with frame records for the given function(s) and
        # we are specifically getting first list from the nest and fetching the third element from the list
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        # log levels are debug -> info -> warning -> error -> critical
        # setting to debug will allow the logger to display all levels when called
        logger.setLevel(logging.DEBUG)
        return logger

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # @pytest.fixture(params=LoginPageData.test_LoginPage_data)
    # def get_data(self, request):
    #     return request.param
