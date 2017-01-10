# coding=UTF-8
import unittest

from tengri import meteoblue as mb
from tengri import yrno as yr
from tengri import mountain as mf


class TestMeteoblue(unittest.TestCase):

    HTML_NAME = 'tests/html/meteoblue.html'

    _root = None

    def get_root(self):
        if self._root is None:
            self._root = mb.get_root(self.HTML_NAME)
        return self._root

    def test_max_temp(self):
        self.assertEqual(u'-13 °C', mb.get_max_temp(self.get_root()))

    def test_min_temp(self):
        self.assertEqual(u'-14 °C', mb.get_min_temp(self.get_root()))

    def test_wind(self):
        self.assertEqual('52 km/h', mb.get_wind(self.get_root()))

    def test_precipation(self):
        self.assertEqual('2-5cm', mb.get_precipation(self.get_root()))


class TestYrNo(unittest.TestCase):

    HTML_NAME = 'tests/html/yrno.html'

    _root = None

    def get_root(self):
        if self._root is None:
            self._root = yr.get_root(self.HTML_NAME)
        return self._root

    def test_temp1(self):
        self.assertEqual(u'-12°', yr.get_temp1(self.get_root()))

    def test_temp2(self):
        self.assertEqual(u'-14°', yr.get_temp2(self.get_root()))

    def test_wind(self):
        text = 'Gentle breeze, 4 m/s from north'
        self.assertEqual(text, yr.get_wind(self.get_root()))

    def test_precipation(self):
        self.assertEqual('0 mm', yr.get_precipation(self.get_root()))


class TestMountainForecast(unittest.TestCase):

    HTML_NAME = 'tests/html/mountain-forecast.html'

    def setUp(self):
        mf.load_html(self.HTML_NAME)

    def test_summary(self):
        value = mf.get_value(mf.LABELS[0])
        self.assertEqual('some clouds', value)

    def test_temp_high(self):
        value = mf.get_value(mf.LABELS[1])
        self.assertEqual('-14', value)

    def test_temp_low(self):
        value = mf.get_value(mf.LABELS[2])
        self.assertEqual('-15', value)

    def test_wind(self):
        value = mf.get_value(mf.LABELS[3])
        self.assertEqual('25', value)

    def test_snow(self):
        value = mf.get_value(mf.LABELS[4])
        self.assertEqual('-', value)

    def test_rain(self):
        value = mf.get_value(mf.LABELS[5])
        self.assertEqual('-', value)
