# Testing Orange HRM Demo Platform
I wanted to test the Orange HR website to practice designing a Python and Selenium automation framework using a Page Object Model. This project has also been integrated with Jenkins to allow for Continuous Integration (CI).

The Login page was tested using a Data-Driven Testing technique pulling the test data, valid and invalid credentials, from an Excel spreadsheet with the help of the Openpyxl library. This technique strengthens the variety and validity of test data, especially during regression testing.

Validating the process of adding a new employee was also tested. The Personal Information Management (PIM) page contains many fields. After the initial adding of an employee with basic information, the website then navigates the user to add more details about the employee. Using the success messages, saving and updating info of an employee could be verified.

All test execution and reporting were handled with Pytest along with the Pytest-html plugin to gelp generate HTML reports. The HTML report captured the test results, making it easy to spot out bugs and analyze results.



