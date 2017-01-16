#!/usr/bin/env python
import argparse
from lxml import html

from pages import meteoblue
from pages import mountain
from pages import yrno

NOT_FOUND = '<not found>'


def _load_value(xpath, root):
    element = root.find(xpath)
    if element is None:
        return NOT_FOUND
    return element.text_content().strip()


def _load_root(path):
    tree = html.parse(path)
    root = tree.getroot()
    return root


def load_html(page):
    root = _load_root(page.TEST_FILE)
    values = []
    for label, elpath in page.ELEMENTS:
        xpath = page.PARENT + elpath
        value = _load_value(xpath, root)
        if value is NOT_FOUND:
            continue
        values.append((label, value))
    return values


def forecast_page(page):
    values = load_html(page)
    print '\n{0}'.format(page.SITE)
    print '-' * len(page.SITE)
    for label, value in values:
        print u'{0}: {1}'.format(label, value)


def forecast(place='Dumbier'):
    print 'Weather for location: {0}'.format(place)

    forecast_page(meteoblue)
    forecast_page(mountain)
    forecast_page(yrno)


def get_arg_parser():
    text = 'Display weather forcasts for specified location'
    parser = argparse.ArgumentParser(description=text)
    # info = 'Location for weather forecast'
    # parser.add_argument('place', help=info)
    return parser


def main():
    parser = get_arg_parser()
    args = parser.parse_args()
    place = getattr(args, 'place', 'Dumbier')
    forecast(place)


if __name__ == "__main__":
    # main()
    forecast()
