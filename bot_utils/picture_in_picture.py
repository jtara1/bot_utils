import mouse
from time import time, sleep
from os.path import basename


from bot_utils import logger
from bot_utils.computer_vision import ComputerVision
from bot_utils.exceptions import TemplateImageNotFound


class PictureInPicture:
    def __init__(self):
        self.vision = ComputerVision()

    def click(self, img_path, double_click=False):
        regions = self.vision.get_matches_from_screen(img_path, threshold=0.95, write_output_image=True)
        img_name = basename(img_path)
        logger.debug('attempting to click %s', img_name)

        if not regions:
            raise TemplateImageNotFound('template image not found: {}'.format(img_path))

        region = regions[0]
        x = (region[0] + region[2]) / 2
        y = (region[1] + region[3]) / 2

        mouse.move(x, y, duration=0.3)
        if double_click:
            mouse.double_click()
        else:
            mouse.click()

    def double_click(self, img_path):
        self.click(img_path, True)

    async def click_asap(self, img_path, double_click=False, timeout=0, attempt_interval=0.2):
        start = time()

        # falsey value for timeout, inf loop & attempts; otherwise, timeout after some time
        while not timeout or (time() - start) / 1000 <= timeout:
            try:
                self.click(img_path, double_click)
                break
            except TemplateImageNotFound:
                sleep(attempt_interval)
