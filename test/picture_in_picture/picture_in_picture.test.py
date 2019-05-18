import os
from os.path import join, dirname, basename, abspath
import unittest
import time

from bot_utils.picture_in_picture.picture_in_picture import PictureInPicture
from bot_utils.picture_in_picture.picture_input import LoadImage, Screenshot

from examples.smt_dx2.images import Images


class TestPip(unittest.TestCase):
    """test picture in picture class"""
    def test_pip(self):
        desktop_img = os.path.join(__file__, '../..', 'images/game-ag.png')
        load_image = LoadImage(desktop_img)
        screenshot = Screenshot()
        picture = PictureInPicture(
            ignore_template_not_found=True, image_similarity_threshold=0.95, picture_input=load_image,
        )
        has_img = picture.has_image(Images.concentrate_status)

        print(f'has demon concentrate status effect image: {has_img}')
        self.assertEqual(has_img, True)

        # next test
        picture.vision.picture_input = screenshot
        has_img_in_ss = False

        for i in range(8):
            if picture.has_image(Images.concentrate_status):
                has_img_in_ss = True
                break
            time.sleep(0.5)
        print(f'has concentrate status image in current screenshot: {has_img_in_ss}')

    def test_darkened_template(self):
        game_img = abspath(join(__file__, '../..', 'images/game-hp.PNG'))
        load_img = LoadImage(game_img)
        print(f'using {game_img}')

        picture = PictureInPicture(
            ignore_template_not_found=True, image_similarity_threshold=0.90, picture_input=load_img
        )
        has_img = picture.has_image(Images.two)
        print(f'hells park has darkened template: {has_img}')
        self.assertTrue(has_img)

    def test_darkened_template_scaled_up(self):
        game_img = abspath(join(__file__, '../..', 'images/game-hp-scaled-up.PNG'))
        load_img = LoadImage(game_img)
        print(f'using {game_img}')

        picture = PictureInPicture(
            ignore_template_not_found=True, image_similarity_threshold=0.90, picture_input=load_img
        )
        has_img = picture.has_image(Images.two)
        print(f'hells park has darkened template in scaled up img: {has_img}')
        self.assertTrue(has_img)


if __name__ == '__main__':
    unittest.main()
