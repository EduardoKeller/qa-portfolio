from playwright.sync_api import Page, expect

def test_homepage_assertions(page: Page):
    page.goto("https://the-internet.herokuapp.com")

    # Texto visível
    expect(page.get_by_text("Welcome to the-internet")).to_be_visible()

    # Heading com texto exato
    expect(page.get_by_role("heading", name="Welcome to the-internet")).to_contain_text("Welcome")

def test_login_assertions(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    # Inputs visíveis e habilitados
    expect(page.get_by_label("Username")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_enabled()

def test_after_login_assertions(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    # URL mudou
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

    # Mensagem de sucesso
    expect(page.locator(".flash.success")).to_be_visible()
    expect(page.locator(".flash.success")).to_contain_text("You logged into a secure area!")

import re
from playwright.sync_api import Page, expect

def test_page_level_assertions(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    # URL exata
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

    # URL por padrão (regex) — mais flexível
    expect(page).to_have_url(re.compile(r"/secure$"))

    # Título da página
    expect(page).to_have_title("The Internet")