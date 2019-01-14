import os
import cv2
import numpy as np
import pyautogui


class ComputerVision:
    def __init__(self):
        pass

    @staticmethod
    def get_matches_from_screen(template_image_path, threshold=0.67, write_output_image=False):
        """finds the bounding box that contains the template image in a screen shot taken
        :returns: tuple of x1, y1, x2, y2
        """
        template_image_path = os.path.abspath(template_image_path)
        image_path = 'gmfs_tmp.png'

        # take screenshot
        pyautogui.screenshot(image_path)

        ### Modified Example from OpenCV Template Matching Example ###
        # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
        img_rgb = cv2.imread(image_path)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template_image_path, 0)
        if not isinstance(template, (list, np.ndarray)):
            raise Exception('file not found or failed or read: {}'.format(template_image_path))
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        regions = []
        for pt in zip(*loc[::-1]):
            # (x1, y1, x2, y2) where x1, y1 is top left, others are bottom right
            regions.append(pt + (pt[0] + w, pt[1] + h))
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        if write_output_image:
            cv2.imwrite('res.png', img_rgb)
        else:
            os.remove(image_path)

        return regions