import pyautogui

from bot_utils.picture_in_picture.picture_input import PictureInputInterface


class Screenshot(PictureInputInterface):
    def get_image(self, save_img_to_path='screenshot.png'):
        pyautogui.screenshot(save_img_to_path)
        return save_img_to_path
