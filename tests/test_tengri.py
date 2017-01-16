# coding=UTF-8
import unittest

if __name__ == '__main__':
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

if True:  # prevent Flake8 warning
    from tengri import tengri
    from tengri.pages import meteoblue as mb


class TestLoadValue(unittest.TestCase):

    _root = None

    def get_root(self):
        if self._root is None:
            self._root = tengri._load_root(mb.TEST_FILE)
        return self._root

    def test_load_value_max_temp(self):
        root = self.get_root()
        path = mb.PARENT + '//div[@class="tab_temp_max"]'
        v = tengri._load_value(path, root)
        self.assertEqual(u'-13 °C', v)

    def test_load_value_not_found(self):
        root = self.get_root()
        path = 'not found'
        v = tengri._load_value(path, root)
        self.assertEqual(tengri.NOT_FOUND, v)


if __name__ == '__main__':
    unittest.main()
