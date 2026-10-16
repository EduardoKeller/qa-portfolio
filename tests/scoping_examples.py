from playwright.sync_api import Page

def test_locator_examples(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    # Fill (clears existing content first)
    page.get_by_label("Username").fill("tomsmith")

    # Type slowly (simulates keystrokes — useful for autocomplete)
    page.get_by_label("Search").type("Python", delay=50)

    # Checkbox
    page.get_by_label("Remember me").check()
    page.get_by_label("Remember me").uncheck()

    # Select dropdown
    page.get_by_label("State").select_option("SP")             # by value
    page.get_by_label("State").select_option(label="Sao Paulo")  # by label
    page.get_by_label("State").select_option(index=2)          # by position

    # File upload
    page.get_by_label("Profile photo").set_input_files("path/to/image.png")


        # Standard click
    page.get_by_role("button", name="Submit").click()

    # Right-click
    page.get_by_text("File").click(button="right")

    # Double-click
    page.get_by_role("row").nth(1).dbl_click()

    # Press a key
    page.get_by_label("Email").press("Tab")
    page.keyboard.press("Control+A")

    # Fill (clears existing content first)
    page.get_by_label("Username").fill("tomsmith")

    # Type slowly (simulates keystrokes — useful for autocomplete)
    page.get_by_label("Search").type("Python", delay=50)

    # Checkbox
    page.get_by_label("Remember me").check()
    page.get_by_label("Remember me").uncheck()

    # Select dropdown
    page.get_by_label("State").select_option("SP")             # by value
    page.get_by_label("State").select_option(label="Sao Paulo")  # by label
    page.get_by_label("State").select_option(index=2)          # by position

    # File upload
    page.get_by_label("Profile photo").set_input_files("path/to/image.png")
