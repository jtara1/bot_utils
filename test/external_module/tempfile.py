import unittest
from time import time

import tempfile


class TestTempfile(unittest.TestCase):
    """test picture in picture class"""
    def test_tempfile(self):
        file = tempfile.NamedTemporaryFile(mode='w')
        file.write('abc')
        contents = open(file.name, 'r').read()
        print(contents)
        print(file.name)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()