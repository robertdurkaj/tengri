#!/usr/bin/env python
import argparse
import requests
import random
from lxml import html

from pages import meteoblue
from pages import mountain
from pages import yrno

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
NOT_FOUND_MSG = 'Place not found on site'
GOOGLE_SEARCH_URL = 'http://www.google.com/search?q={0}'


def _load_value(xpath, root):
    element = root.find(xpath)
    if element is None:
        return NOT_FOUND
    return element.text_content().strip()


def _load_root_from_file(path):
    tree = html.parse(path)
    root = tree.getroot()
    return root


def _load_root_from_string(str):
    root = html.fromstring(str)
    return root


def load_html(page, response):
    root = _load_root_from_string(response.text)
    values = []
    for label, elpath in page.ELEMENTS:
        xpath = page.PARENT + elpath
        value = _load_value(xpath, root)
        if value is NOT_FOUND:
            continue
        values.append((label, value))
    return values


def get_response(url):
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
    query = 'site:{0}+{1}'.format(site, place)
    return GOOGLE_SEARCH_URL.format(query)


def get_first_link(root):
    a = root.find('.//*[@class="r"]/a')
    if a is None:
        return NOT_FOUND
    return a.attrib['href']


def forecast_page(page, place):
    print '\n{0}'.format(page.SITE)
    print '-' * len(page.SITE)

    try:
        url = prepare_query(page.SITE, place)
        r = get_response(url)
        root = _load_root_from_string(r.text)
        link_url = get_first_link(root)
        if link_url == NOT_FOUND:
            print NOT_FOUND_MSG
            return

        r = get_response(link_url)

        values = load_html(page, r)
        for label, value in values:
            print u'{0}: {1}'.format(label, value)
    except requests.exceptions.ConnectionError:
        print 'Network connection error'


def forecast(place):
    print 'Weather for location: {0}'.format(place)

    for page in (meteoblue, mountain, yrno):
        forecast_page(page, place)


def get_arg_parser():
    text = 'Display weather forcasts for specified location'
    parser = argparse.ArgumentParser(description=text)
    info = 'Location for weather forecast'
    parser.add_argument('place', help=info)
    return parser


def main():
    parser = get_arg_parser()
    args = parser.parse_args()
    place = getattr(args, 'place', 'Dumbier')
    forecast(place)


if __name__ == "__main__":
    main()
