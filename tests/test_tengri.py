# -*- coding: utf-8 -*-
"""
    tests.tengri
    -----------------

    Unit tests.

    :copyright: (c) 2017 by Robert Durkaj.
    :license: MIT, see the LICENSE for more details.
"""
import pytest
import mock
import io

from tengri import weather
from tengri import web


@pytest.fixture(scope="module")
def root():
    test_file = 'tests/fixtures/meteoblue.html'
    return weather._load_root_from_file(test_file)


def test_load_value_max_temp(root):
    """ Test for specific value `max_temp` """

    xpath = './/div[@id="day2"]//div[@class="tab_temp_max"]'
    v = weather._load_value(xpath, root)
    assert v == u'-13 °C'


def test_load_value_not_found(root):
    """ Test value not found situation """

    path = 'not found'
    v = weather._load_value(path, root)
    assert v == weather.NOT_FOUND


def test_get_first_link_no_results():
    """ Test no results situation """

    html_string = '<html><body><p>No results</p></body></html>'
    root = weather._load_root_from_string(html_string)
    v = weather.get_first_link(root)
    assert v == weather.NO_RESULTS


def test_load_html_empty_result():
    """ Test load_html function """

    htmltext = "<html></html>"
    page = dict(lines=(('', './/div[@id="day2"]'),))
    values = weather.load_html(page, htmltext)
    assert values == []


def test_load_html_with_result():
    """ Test load_html function """

    text = "content"
    htmltext = "<html><div id='day2'>{0}</div></html>".format(text)
    page = dict(lines=(('label', './/div[@id="day2"]'),))
    values = weather.load_html(page, htmltext)
    assert values == [('label', text)]


def test_prepare_query():
    """ Test prepare_query function """

    site = r'http://www.test.org'
    place = 'Khan Tengri'
    result = weather.prepare_query(site, place)
    assert result.startswith(weather.GOOGLE_SEARCH_URL[:-3])


def test_get_valid_place_empty():
    """ Test get_valid_place function """

    with pytest.raises(ValueError):
        weather.get_valid_place('    ')


def test_get_valid_place_spaces():
    """ Test get_valid_place function """

    assert "Tengri" == weather.get_valid_place("  Tengri  ")


def test_get_arg_parser():
    """ Test get_arg_parser function """

    p = weather.get_arg_parser()
    assert p.description is not None

    a = p.parse_args('Khan Tengri'.split())
    assert a.place == ['Khan', 'Tengri']


def test_weather_pages():
    """ Test weather_pages function. """

    assert len(web.weather_pages()) == 3


def test_forecast_page_noresult():
    """ Test forecast_page function """

    weather.get_result_url = mock.Mock(return_value=weather.NO_RESULTS)
    weather.forecast_page(web._meteoblue_page(), "place")


def test_forecast_page_success():
    """ Test forecast_page function """

    with io.open('tests/fixtures/meteoblue.html', encoding='utf-8') as f:
        html = f.read()

    weather.get_result_url = mock.Mock(return_value="url")
    weather.get_response_text = mock.Mock(return_value=html)
    weather.forecast_page(web._meteoblue_page(), "place")


def test_forecast():
    """ Test main forecast function """

    weather.forecast_page = mock.Mock(return_value=None)
    weather.forecast("place")
