from .base_page import BasePage

class SecurePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.heading    = page.get_by_role("heading", name="Secure Area")
        self.logout_btn = page.get_by_role("link", name="Logout")

    def logout(self):
        self.logout_btn.click()

    def is_visible(self) -> bool:
        return self.heading.is_visible()