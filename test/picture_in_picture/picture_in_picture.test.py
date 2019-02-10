import unittest

from bot_utils.picture_in_picture.picture_in_picture import PictureInPicture

from examples.smt_dx2.images import Images


class TestPip(unittest.TestCase):
    """test picture in picture class"""
    def test_pip(self):
        picture = PictureInPicture()
        region = picture.click(Images.concentrate_status)
        print(region)
        # self.assertEqual(region.center, (50, 50))


if __name__ == '__main__':
    unittest.main()
