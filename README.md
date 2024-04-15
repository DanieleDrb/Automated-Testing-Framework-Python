# Automated-Testing-Framework-Python
Automated Testing Framework for Registration Process
This project is an automated testing framework built with Python, Pytest, and Allure to test the registration process of a web application. It aims to provide comprehensive testing coverage for various scenarios encountered during user registration.

Features
Pytest: Utilizes Pytest, a testing framework for Python, to write and execute test cases efficiently.
Allure Reporting: Integrates Allure Reporting for generating comprehensive and interactive test reports.
Selenium WebDriver: Uses Selenium WebDriver to automate interactions with the web application's UI elements.
Parameterized Tests: Employs parameterized tests to test various input combinations for robust validation.
Page Object Model (POM): Implements the Page Object Model design pattern for better test maintenance and readability.
Prerequisites
Ensure you have the following installed:

Python 3.x
Pip package manager
Webdriver compatible with your browser (e.g., GeckodriverDriver for Firefox)

To Use Allure:
You need to run your tests with --> pytest --alluredir=./allure-results 'your_test'
And then use --> allure serve ./allure-results 
