import random
import string

from selene.support.shared import browser
from selene import be, have
from datetime import date


def test_positive(browser_actions):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative(browser_actions):
    res = date.today().strftime("%Y%b%d").join(random.choices(string.ascii_uppercase + string.digits, k=15))
    browser.element('[name="q"]').type(res).press_enter()
    browser.element('#result-stats').should(have.text('About 0 results'))
