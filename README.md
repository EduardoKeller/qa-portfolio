# QA Portfolio — Playwright + Python

Test automation project built while learning Playwright with Python.  
Tests run against [The Internet](https://the-internet.herokuapp.com/), a free practice app for QA automation.

---

## Stack

- **Playwright** — browser automation
- **pytest** — test runner
- **pytest-playwright** — Playwright fixtures for pytest  
- **pytest-html** — HTML reports
- **GitHub Actions** — runs tests on every push

---

## Structure

qa-portfolio/
├── pages/ # Page Object Model
│ ├── base_page.py
│ ├── login_page.py
│ └── secure_page.py
├── tests/
│ ├── conftest.py # video recording + tracing fixtures
│ ├── test_homepage.py
│ ├── test_navigation.py
│ ├── test_assertions.py
│ └── test_login.py # parametrized login scenarios
├── .github/workflows/
│ └── playwright.yml # CI pipeline
├── pytest.ini
└── requirements.txt


---

## Running locally

```bash
pip install -r requirements.txt
playwright install chromium
pytest
```

Run only smoke tests:
```bash
pytest -m smoke
```

Run with visible browser:
```bash
pytest --headed
```

---

## Reports

After a test run, open `reports/report.html` in the browser.  
To inspect a trace: `playwright show-trace reports/trace.zip`

---

## Author

Eduardo Pasquali Keller — [GitHub](https://github.com/EduardoKeller)
