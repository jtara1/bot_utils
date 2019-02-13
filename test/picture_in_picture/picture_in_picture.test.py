import os
import unittest
import time

from bot_utils.picture_in_picture.picture_in_picture import PictureInPicture
from bot_utils.picture_in_picture.picture_input import LoadImage, Screenshot

from examples.smt_dx2.images import Images


class TestPip(unittest.TestCase):
    """test picture in picture class"""
    def test_pip(self):
        desktop_img = os.path.join(__file__, '../..', 'images/desktop.png')
        load_image = LoadImage(desktop_img)
        screenshot = Screenshot()
        picture = PictureInPicture(
            ignore_template_not_found=True, image_similarity_threshold=0.95, picture_input=load_image,
        )
        has_img = picture.has_image(Images.concentrate_status)
        print(f'has concentrate status image: {has_img}')

        self.assertEqual(has_img, True)

        picture.vision.picture_input = screenshot

        has_img_in_ss = False
        for i in range(8):
            if picture.has_image(Images.concentrate_status):
                has_img_in_ss = True
                break
            time.sleep(0.5)
        print(f'has concentrate status image in current screenshot: {has_img_in_ss}')


if __name__ == '__main__':
    unittest.main()
