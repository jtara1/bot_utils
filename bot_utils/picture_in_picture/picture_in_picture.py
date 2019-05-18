import mouse
from time import time, sleep
from os.path import basename

from bot_utils import logger
from bot_utils.picture_in_picture.computer_vision import ComputerVision
from bot_utils.picture_in_picture.region import Region
from bot_utils.picture_in_picture.picture_input import Screenshot
from bot_utils.exceptions import TemplateImageNotFound


class PictureInPicture:
    def __init__(self, ignore_template_not_found=False, image_similarity_threshold=0.95, picture_input=Screenshot()):
        """search for a picture in a picture (screenshot) aka does image template matching"""
        self.ignore_template_not_found = ignore_template_not_found
        self.vision = ComputerVision(image_similarity_threshold=image_similarity_threshold, picture_input=picture_input)

    def get_regions(self, img_path):
        """finds all instances of the image & returns the regions"""
        return self.vision.get_matches_from_screen(img_path, write_output_image=True)

    def has_image(self, img_path):
        """image is present"""
        return not not self.get_regions(img_path)

    async def has_image_within_period(self, img_path, time_period=3.5, frequency_for_check=0.1):
        """image is present within period of time

        :param img_path:
        :param time_period: in seconds
        :param frequency_for_check: in seconds
        :return: bool
        """
        start = time()
        while (time() - start) <= time_period:
            if self.has_image(img_path):
                return True
            sleep(frequency_for_check)

        return False

    def click(self, img_path, double_click=False):
        logger.debug('attempting to click %s', basename(img_path))

        regions = self.get_regions(img_path)

        if not regions:
            msg = 'template image not found: {}'.format(img_path)
            if not self.ignore_template_not_found:
                raise TemplateImageNotFound(msg)
            logger.debug(msg)

        else:
            region = regions[0]
            mouse.move(*region.center, duration=0.3)
            mouse.double_click() if double_click else mouse.click()
            return region

        return Region()  # emtpy region / list

    def double_click(self, img_path):
        self.click(img_path, True)

    async def click_asap(self, img_path, double_click=False, timeout=0, attempt_interval=0.2):
        """click as soon as possible"""
        start = time()

        # falsey value for timeout, inf loop & attempts; otherwise, timeout after some time
        while not timeout or (time() - start) <= timeout:
            try:
                self.click(img_path, double_click)
                break
            except TemplateImageNotFound:
                sleep(attempt_interval)
