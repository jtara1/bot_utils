import os
import shutil
from os.path import join, basename
from time import time

import pyautogui

from bot_utils.picture_in_picture.picture_input import PictureInputInterface


class Screenshot(PictureInputInterface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.screenshots_folder = join(__file__, '..', 'screenshots')
        os.makedirs(self.screenshots_folder, exist_ok=True)

    def get_image(self, save_img_to_path='screenshot.png'):
        pyautogui.screenshot(save_img_to_path)
        if self.debug:
            extension = basename(save_img_to_path).split('.')[-1]
            shutil.copyfile(save_img_to_path, join(self.screenshots_folder, f'{time()}.{extension}'))
        return save_img_to_path
