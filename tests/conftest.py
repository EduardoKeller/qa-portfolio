import pytest


@pytest.fixture
def page(browser):
    context = browser.new_context(record_video_dir="reports/videos/")
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()
    yield page
    context.tracing.stop(path="reports/trace.zip")
    context.close()