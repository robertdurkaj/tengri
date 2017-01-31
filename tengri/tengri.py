#!/usr/bin/env python
# coding=UTF-8
"""
    tengri
    -----------------

    Display weather forecast for specified location.

    :copyright: (c) 2017 by Robert Durkaj.
    :license: MIT, see the LICENSE for more details.
"""
import argparse
import random

import requests
from lxml import html

from pages import meteoblue, mountain, yrno

# User-Agents from "http://useragentstring.com"
USER_AGENTS = (
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/41.0.2227.1 Safari/537.36'),
    ('Mozilla/5.0 (Windows NT 6.1) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/41.0.2228.0 Safari/537.36'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) '
     'AppleWebKit/602.3.12 (KHTML, like Gecko) '
     'Version/10.0.2 Safari/602.3.12'),
    'Mozilla/5.0 (Windows NT 6.1; x64; rv:25.0) Gecko/20100101 Firefox/29.0',
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) '
     'Gecko/20100101 Firefox/33.0'),
    'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
)
NOT_FOUND = '<not found>'
GOOGLE_SEARCH_URL = 'http://www.google.com/search?q={0}'
NO_RESULTS = '<no results>'
NO_RESULTS_MSG = 'Place not found on site'


def _load_value(xpath, root):
    """ Return text content of the first element specified by `xpath`.
    :param str xpath: XPath of the element.
    :param root: Root element.
    """

    element = root.find(xpath)  # type: html.HtmlElement
    if element is None:
        return NOT_FOUND
    value = element.text_content()
    value = ' '.join(value.split())  # remove unwanted space characters
    return value


def _load_root_from_file(path):
    """ Return root element from HTML file.
    :param str path: The path of HTML file.
    """

    tree = html.parse(path)
    root = tree.getroot()  # type: html.HtmlElement
    return root


def _load_root_from_string(text):
    """ Return root element of HTML passed as `text`. """

    root = html.fromstring(text)
    return root


def load_html(page, response):
    """ Return values found in HTML response. """

    root = _load_root_from_string(response.text)
    values = []
    for label, xpath in page.LINES:
        value = _load_value(xpath, root)
        if value is not NOT_FOUND:
            values.append((label, value))
    return values


def get_response(url):
    """ Return HTML response from `url`. """

    user_agent = random.choice(USER_AGENTS)
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, timeout=2.0)

    # TODO use logging
    # print '\nRequesting: {0}'.format(url)
    # print 'User-Agent: {0}'.format(user_agent)
    # print 'content-type: {0}'.format(r.headers['content-type'])
    # print 'headers: {0}'.format(r.headers)
    # print 'history: {0}'.format(r.history)
    # print 'Response: {0}\n'.format(r.status_code)

    return r


def prepare_query(site, place):
    """ Return search query for `site` and `place`. """

    query = 'site:{0}+{1}'.format(site, place)
    return GOOGLE_SEARCH_URL.format(query)


def get_first_link(root):
    """ Return first result from `root` element. """

    a = root.find('.//*[@class="r"]/a')
    if a is None:
        return NO_RESULTS
    return a.attrib['href']


def forecast_page(page, place):
    """ Process weather forecast for `page` and `place. Print all values. """

    print '\n{0}'.format(page.SITE)
    print '-' * len(page.SITE)

    try:
        url = prepare_query(page.SITE, place)
        r = get_response(url)
        root = _load_root_from_string(r.text)
        link_url = get_first_link(root)
        if link_url == NO_RESULTS:
            print NO_RESULTS_MSG
            return

        r = get_response(link_url)

        values = load_html(page, r)
        for label, value in values:
            print u'{0}: {1}'.format(label, value)
    except requests.exceptions.ConnectionError:
        print 'Network connection error'


def forecast(place):
    """ Main forecast function. """

    print '\nTengri weather report for: "{0}"'.format(place)
    for page in (meteoblue, mountain, yrno):
        forecast_page(page, place)
    print ''


def get_arg_parser():
    """ Return cmd argument parser. """

    text = 'Display weather forcasts for specified location'
    parser = argparse.ArgumentParser(description=text)
    info = 'Location for weather forecast'
    parser.add_argument('place', nargs='+', help=info)
    return parser


def cmd_launcher():
    """ Main entry point of application. """

    parser = get_arg_parser()
    args = parser.parse_args()
    place = getattr(args, 'place', 'Dumbier')
    place = ' '.join(place)
    forecast(place)


if __name__ == "__main__":
    cmd_launcher()
