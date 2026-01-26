import allure
import pytest
from pageObjects.login import LoginPage

@allure.feature("Login")
class TestLogin:

    @pytest.mark.parametrize("email,password", [
        ("wrongmail.com", "WrongPass123"),
        ("g.sheakher@gmail.com", "WrongPassword")
    ])
    def test_invalid_login(self, browserInstance, email, password):
        login = LoginPage(browserInstance)
        status = login.login(email, password)

        with allure.step("Verify login failure"):
            assert status in ["INVALID_EMAIL", "INVALID_PASSWORD"]

    def test_valid_login(self, browserInstance):
        login = LoginPage(browserInstance)
        status = login.login("g.sheakher@gmail.com", "Somearti@1993")

        assert status == "LOGIN_SUCCESS"
