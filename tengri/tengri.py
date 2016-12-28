#!/usr/bin/env python
import argparse
import meteoblue
import yrno


def tengri(place='Dumbier'):
    print 'Weather for location: {0}'.format(place)
    print '\nmeteoblue.com\n-------------'
    meteoblue.forecast()
    print '\nyr.no\n-----'
    yrno.forecast()


def get_parser():
    text = 'Display weather forcasts for specified location'
    parser = argparse.ArgumentParser(description=text)
    # info = 'Location for weather forecast'
    # parser.add_argument('place', help=info)
    return parser


def command_line_runner():
    parser = get_parser()
    args = parser.parse_args()
    place = getattr(args, 'place', 'Dumbier')
    tengri(place)


if __name__ == "__main__":
    command_line_runner()
