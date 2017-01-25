# coding=UTF-8
"""
    tests.tengri
    -----------------

    Unit tests.

    :copyright: (c) 2017 by Robert Durkaj.
    :license: MIT, see the LICENSE for more details.
"""
import pytest

from tengri import tengri
from tengri.pages import meteoblue


@pytest.fixture(scope="module")
def root():
    return tengri._load_root_from_file(meteoblue.TEST_FILE)


def test_load_value_max_temp(root):
    xpath = './/div[@id="day2"]//div[@class="tab_temp_max"]'
    v = tengri._load_value(xpath, root)
    assert v == u'-13 °C'


def test_load_value_not_found(root):
    path = 'not found'
    v = tengri._load_value(path, root)
    assert v == tengri.NOT_FOUND


def test_get_first_link_not_found():
    html_string = '<html><body><p>No links</p></body></html>'
    root = tengri._load_root_from_string(html_string)
    v = tengri.get_first_link(root)
    assert v == tengri.NOT_FOUND
