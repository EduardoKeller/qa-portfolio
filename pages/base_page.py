from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = ""):
        self.page.goto("https://the-internet.herokuapp.com" + path)

    def get_title(self) -> str:
        return self.page.title()

    def screenshot(self, name: str):
        self.page.screenshot(path=f"reports/{name}.png")