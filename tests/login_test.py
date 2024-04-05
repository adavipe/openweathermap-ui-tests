import allure
import pytest

from config import data
from pages.login_page import LoginPage


@allure.feature("Login Functionality")
class TestLogin:

    @allure.title("Login with valid data")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_login_with_invalid_data(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(data.Data.EMAIL)
        login_page.enter_password(data.Data.PASSWORD)
        login_page.click_submit_button()
        # здесь будет assert на появление алерта (div[class="panel-body"] с текстом "Invalid Email or password.")
        # здесь будет assert на то, что url остался тот же
        login_page.make_screenshot("Invalid Email or password")

