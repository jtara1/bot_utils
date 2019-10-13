import os
import shutil
from os.path import join, basename, abspath
from time import time

import pyautogui

from bot_utils.picture_in_picture.picture_input import PictureInputAbstractClass
from bot_utils.picture_in_picture.region import Region


class Screenshot(PictureInputAbstractClass):
    def __init__(self, crop_region=(0, 221, 2067, 1090), *args, **kwargs):
        """

        :param crop_region: <Region>
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)

        self.screenshots_folder = abspath(join(__file__, '..', 'screenshots'))
        os.makedirs(self.screenshots_folder, exist_ok=True)

        self.crop_region = Region(crop_region)

    def get_image(self, save_img_to_path='screenshot.png'):
        super().get_image(save_img_to_path)

        pyautogui.screenshot(self.img_path, region=self.crop_region)
        if self.debug:
            extension = basename(self.img_path).split('.')[-1]
            shutil.copyfile(self.img_path, join(self.screenshots_folder, f'{time()}.{extension}'))
        return self.img_path

    def update_region(self, region):
        offset_x, offset_y = [self.crop_region[0], self.crop_region[1]]
        return Region([region[0] + offset_x, region[1] + offset_y, region[2] + offset_x, region[3] + offset_y])
