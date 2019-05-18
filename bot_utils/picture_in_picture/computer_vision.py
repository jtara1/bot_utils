import os
from os.path import abspath
import cv2
import numpy as np
import imutils

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

        # load the image image, convert it to grayscale, and detect edges
        template = cv2.imread(template_image_path)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        template = cv2.Canny(template, 50, 200)
        (tH, tW) = template.shape[:2]
        # cv2.imshow("Template", template)

        # load the image, convert it to grayscale, and initialize the
        # bookkeeping variable to keep track of the matched region
        img_rgb = cv2.imread(image_path)
        gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        found = None

        # loop over the scales of the image
        for scale in np.linspace(0.2, 1.0, 20)[::-1]:
            # resize the image according to the scale, and keep track
            # of the ratio of the resizing
            resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
            r = gray.shape[1] / float(resized.shape[1])

            # if the resized image is smaller than the template, then break
            # from the loop
            if resized.shape[0] < tH or resized.shape[1] < tW:
                break

            # detect edges in the resized, grayscale image and apply template
            # matching to find the template in the image
            edged = cv2.Canny(resized, 50, 200)
            result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

            # check to see if the iteration should be visualized
            # draw a bounding box around the detected region
            clone = np.dstack([edged, edged, edged])
            cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
                          (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
            # cv2.imshow("Visualize", clone)
            # cv2.waitKey(0)

            # if we have found a new maximum correlation value, then update
            # the bookkeeping variable
            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, r)

        if self.debug or write_output_image:
            cv2.imwrite('res.png', img_rgb)
        self.picture_input.clean()

        # unpack the bookkeeping variable and compute the (x, y) coordinates
        # of the bounding box based on the resized ratio
        (_, maxLoc, r) = found
        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

        # draw a bounding box around the detected result and display the image
        cv2.rectangle(img_rgb, (startX, startY), (endX, endY), (0, 0, 255), 2)
        # cv2.imshow("Image", image)
        # cv2.waitKey(0)

        return [Region([startX, startY, endX, endY])]
