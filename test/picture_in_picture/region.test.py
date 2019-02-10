import unittest

from bot_utils.picture_in_picture.region import Region


class TestPip(unittest.TestCase):
    """test picture in picture class"""
    def test_region(self):
        region = Region([0, 0, 100, 101])
        self.assertEqual(region.center, (50, 50))


if __name__ == '__main__':
    unittest.main()