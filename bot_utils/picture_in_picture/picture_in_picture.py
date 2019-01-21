import mouse
from time import time, sleep
from os.path import basename


from bot_utils import logger
from bot_utils.picture_in_picture.computer_vision import ComputerVision
from bot_utils.exceptions import TemplateImageNotFound


class PictureInPicture:
    def __init__(self):
        """search for a picture in a picture (screenshot) aka does image template matching"""
        self.vision = ComputerVision(image_similarity_threshold=0.95)

    def _get_regions(self, img_path):
        """finds all instances of the image & returns the regions"""
        return self.vision.get_matches_from_screen(img_path, write_output_image=True)

    def has_image(self, img_path):
        """image is present"""
        return not not self._get_regions(img_path)

    def click(self, img_path, double_click=False):
        logger.debug('attempting to click %s', basename(img_path))

        regions = self._get_regions(img_path)
        if not regions:
            raise TemplateImageNotFound('template image not found: {}'.format(img_path))

        region = regions[0]
        mouse.move(*region.center, duration=0.3)
        mouse.double_click() if double_click else mouse.click()

    def double_click(self, img_path):
        self.click(img_path, True)

    async def click_asap(self, img_path, double_click=False, timeout=0, attempt_interval=0.2):
        """click as soon as possible"""
        start = time()

        # falsey value for timeout, inf loop & attempts; otherwise, timeout after some time
        while not timeout or (time() - start) / 1000 <= timeout:
            try:
                self.click(img_path, double_click)
                break
            except TemplateImageNotFound:
                sleep(attempt_interval)
