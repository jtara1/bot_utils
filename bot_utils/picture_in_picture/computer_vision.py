import os
from os.path import abspath, basename

import cv2
import numpy as np
import imutils

from bot_utils.picture_in_picture.region import Region
from bot_utils.picture_in_picture.picture_input import Screenshot
from bot_utils.utils import DebugAbstractClass
from bot_utils.utils.exceptions import TemplateImageNotFound


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

        # take screenshot
        image_path = abspath(self.picture_input.get_image('temp-pic-input.png'))

        # load the image image, convert it to grayscale, and detect edges
        template = cv2.imread(template_image_path)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        template = cv2.Canny(template, 50, 200)
        (template_height, template_width) = template.shape[:2]
        # cv2.imshow("Template", template)

        # load the image, convert it to grayscale, and init the bookkeeping var to keep track of the matched region
        img_rgb = cv2.imread(image_path)
        gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        found = None

        # loop over the scales of the image
        for scale in np.linspace(0.2, 1.0, 20)[::-1]:
            # resize the image according to the scale, and keep track of the ratio of the resizing
            resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
            resize_ratio = gray.shape[1] / float(resized.shape[1])

            # if the resized image is smaller than the template, then break from the loop
            if resized.shape[0] < template_height or resized.shape[1] < template_width:
                break

            # detect edges in the resized, grayscale image and apply template matching to find the template in the image
            edged = cv2.Canny(resized, 50, 200)
            match_result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
            # minVal, maxVal, minLoc, maxLoc
            (_, max_val, _, match_location) = cv2.minMaxLoc(match_result)  # finds the most similar match

            # check to see if the iteration should be visualized draw a bounding box around the detected region
            clone = np.dstack([edged, edged, edged])
            cv2.rectangle(clone, (match_location[0], match_location[1]),
                          (match_location[0] + template_width, match_location[1] + template_height), (0, 0, 255), 2)
            # cv2.imshow("Visualize", clone)
            # cv2.waitKey(0)

            # if we have found a new maximum correlation value, then update the bookkeeping variable
            if found is None or max_val > found[0]:
                found = (max_val, match_location, resize_ratio, match_result)

        # unpack the bookkeeping variable and compute the (x, y) coordinates
        # of the bounding box based on the resized ratio
        (_, match_location, resize_ratio, match_result) = found
        normalized = match_result / np.linalg.norm(match_result)
        (_, normalized_max_value, _, _) = cv2.minMaxLoc(normalized)  # finds the most similar match

        if normalized_max_value <= 0.012:
            raise TemplateImageNotFound(f'template img not found: {basename(template_image_path)}')

        (startX, startY) = (int(match_location[0] * resize_ratio), int(match_location[1] * resize_ratio))
        (endX, endY) = (
            int((match_location[0] + template_width) * resize_ratio),
            int((match_location[1] + template_height) * resize_ratio))

        # draw a bounding box around the detected result and display the image
        cv2.rectangle(img_rgb, (startX, startY), (endX, endY), (0, 0, 255), 2)
        # cv2.imshow("Image", img_rgb)
        # cv2.waitKey(0)

        if self.debug or write_output_image:
            cv2.imwrite('debug.png', img_rgb)
        self.picture_input.clean()

        match_region = Region([startX, startY, endX, endY])
        return [self.picture_input.update_region(match_region)]
