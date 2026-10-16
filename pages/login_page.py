class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/login"
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.submit   = page.get_by_role("button", name="Login")
        self.flash    = page.locator(".flash")

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()

    def get_flash(self) -> str:
        return self.flash.text_content().strip()