import os
import unittest

from bot_utils.picture_in_picture.picture_in_picture import PictureInPicture
from bot_utils.picture_in_picture.picture_input import LoadImage

from examples.smt_dx2.images import Images


class TestPip(unittest.TestCase):
    """test picture in picture class"""
    def test_pip(self):
        desktop_img = os.path.join(__file__, '../..', 'images/desktop.png')
        picture = PictureInPicture(
            ignore_template_not_found=True, image_similarity_threshold=0.95, picture_input=LoadImage(desktop_img)
        )
        has_img = picture.has_image(Images.concentrate_status)
        print(f'has concentrate status image: {has_img}')

        self.assertEqual(has_img, True)


if __name__ == '__main__':
    unittest.main()
