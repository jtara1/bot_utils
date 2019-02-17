import os
from os.path import abspath
import cv2
import numpy as np

from bot_utils.picture_in_picture.region import Region
from bot_utils.picture_in_picture.picture_input import Screenshot
from bot_utils.utils import DebugAbstractClass


class ComputerVision(DebugAbstractClass):
    def __init__(self, image_similarity_threshold=0.90, picture_input=Screenshot()):
        """does the actual template matching"""
        super().__init__()

        self.image_similarity_threshold = image_similarity_threshold
        self.picture_input = picture_input

    def get_matches_from_screen(self, template_image_path, write_output_image=False):
        """finds the bounding box that contains the template image in a screen shot taken
        :returns: tuple of x1, y1, x2, y2
        """
        template_image_path = abspath(template_image_path)
        image_path = 'gmfs_tmp.png'

        # take screenshot
        image_path = abspath(self.picture_input.get_image(image_path))

        ### Modified Example from OpenCV Template Matching Example ###
        # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
        img_rgb = cv2.imread(image_path)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template_image_path, 0)
        if not isinstance(template, (list, np.ndarray)):
            raise Exception('file not found or failed or read: {}'.format(template_image_path))
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= self.image_similarity_threshold)
        regions = []
        for pt in zip(*loc[::-1]):
            # (x1, y1, x2, y2) where x1, y1 is top left, others are bottom right
            coords = list(pt + (pt[0] + w, pt[1] + h))
            regions.append(Region(coords))
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 5)

        if self.debug or write_output_image:
            cv2.imwrite('res.png', img_rgb)
        self.picture_input.clean()

        return regions
