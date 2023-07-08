import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# clear driver globally so driver in _capture_screenshot can reference driver defined in setup
driver = None


# hook code for passing in command line options into pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# scope is set to class for setup() to be executed once before test cases
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service_obj = Service("/Users/neilsoriano/Drivers/chromedriver")
        driver = webdriver.Chrome(options=options, service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("/Users/neilsoriano/Drivers/geckodriver")
        driver = webdriver.Firefox(service=service_obj)

    driver.implicitly_wait(4)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # assign local driver of this fixture to the class driver
    request.cls.driver = driver
    yield
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
