import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_page_loads(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert page.get_by_label("Username").is_visible()

@pytest.mark.parametrize("username,password,expected", [
    ("tomsmith",  "SuperSecretPassword!", "You logged into a secure area!"),
    ("wronguser", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith",  "wrongpassword",        "Your password is invalid!"),
    ("",          "",                     "Your username is invalid!"),
])
@pytest.mark.regression
def test_login_scenarios(page: Page, username, password, expected):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    assert expected in page.locator(".flash").text_content()

@pytest.mark.smoke
@pytest.mark.regression
def test_login_with_pom(page: Page):
    login = LoginPage(page)
    login.navigate()
    login.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login.get_flash()