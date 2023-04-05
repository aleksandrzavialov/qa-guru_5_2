import pytest
from selene.support.shared import browser
from selene import command


@pytest.fixture(scope='session')
def browser_actions():
    browser.config.window_width = 1280
    browser.config.window_height = 1024
    browser.open('https://google.com')
    # Accept cookies
    browser.element('#L2AGLb').perform(command.js.scroll_into_view).click()
    yield 'finished'
    browser.close()
