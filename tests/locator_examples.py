from playwright.sync_api import Page

def test_locator_examples(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    # 1. Role — most resilient, matches ARIA semantics
    page.get_by_role("button", name="Login")
    page.get_by_role("textbox", name="Username")
    page.get_by_role("link", name="Forgot Password")

    # 2. Label — best for form inputs
    page.get_by_label("Username")
    page.get_by_label("Password")

    # 3. Placeholder text
    page.get_by_placeholder("Enter username")

    # 4. Visible text
    page.get_by_text("Login")
    page.get_by_text("Login", exact=True)

    # 5. Test ID (data-testid attribute)
    page.get_by_test_id("submit-button")

    # 6. CSS selector — last resort
    page.locator("button#login")
    page.locator(".flash.success")