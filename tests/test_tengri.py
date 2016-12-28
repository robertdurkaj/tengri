import unittest
import context

from tengri import meteoblue as mb
from tengri import yrno as yr

# prevent unused warning
assert context


class TestMeteoblue(unittest.TestCase):

    HTML_NAME = 'tests/html/meteoblue.html'

    _root = None

    def get_root(self):
        if self._root is None:
            self._root = mb.get_root(self.HTML_NAME)
        return self._root

    def test_max_temp(self):
        self.assertEqual(u'-13 \xb0C', mb.get_max_temp(self.get_root()))

    def test_min_temp(self):
        self.assertEqual(u'-14 \xb0C', mb.get_min_temp(self.get_root()))

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

    def test_max_temp(self):
        self.assertEqual(u'-14\xb0', yr.get_max_temp(self.get_root()))

    def test_min_temp(self):
        self.assertEqual(u'-12\xb0', yr.get_min_temp(self.get_root()))

    def test_wind(self):
        text = 'Gentle breeze, 4 m/s from north'
        self.assertEqual(text, yr.get_wind(self.get_root()))

    def test_precipation(self):
        self.assertEqual('0 mm', yr.get_precipation(self.get_root()))


if __name__ == '__main__':
    unittest.main()
