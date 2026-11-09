import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.navigate()
    return login


@pytest.mark.smoke
def test_login_page_loads(login_page: LoginPage):
    assert login_page.username.is_visible()
    assert login_page.password.is_visible()
    assert login_page.submit.is_visible()


@pytest.mark.parametrize("username,password,expected", [
    ("tomsmith",  "SuperSecretPassword!", "You logged into a secure area!"),
    ("wronguser", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith",  "wrongpassword",        "Your password is invalid!"),
    ("",          "",                     "Your username is invalid!"),
], ids=["valid_credentials", "invalid_username", "invalid_password", "empty_fields"])
@pytest.mark.regression
def test_login_scenarios(login_page: LoginPage, username, password, expected):
    login_page.login(username, password)
    assert expected in login_page.get_flash()


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_login_redirects_to_secure_area(login_page: LoginPage):
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert login_page.page.url.endswith("/secure")
    assert "You logged into a secure area!" in login_page.get_flash()
