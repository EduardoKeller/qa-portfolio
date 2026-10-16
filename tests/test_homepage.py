from playwright.sync_api import Page

def test_page_title(page: Page):
    page.goto("https://the-internet.herokuapp.com")
    assert "The Internet" in page.title()

def test_heading_visible(page: Page):
    page.goto("https://the-internet.herokuapp.com")
    heading = page.get_by_role("heading", name="Welcome to the-internet")
    assert heading.is_visible()

