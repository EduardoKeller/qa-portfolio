from playwright.sync_api import Page

def test_homepage_loads(page: Page):
    page.goto("https://the-internet.herokuapp.com")
    assert "The Internet" in page.title()

def test_login_page_loads(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert page.get_by_label("Username").is_visible()