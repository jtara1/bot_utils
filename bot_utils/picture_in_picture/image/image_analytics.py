import cv2
import numpy as np
from skimage import io

from bot_utils.picture_in_picture.image.rgb_color import RGBColor


class ImageAnalytics:
    def __init__(self, image_file_path, crop_region=None):
        self.image_file_path = image_file_path
        # self.image = cv2.imread(image_file_path)
        self.image = io.imread(image_file_path)

        if crop_region:
            x, y, x2, y2 = crop_region
            self.image = self.image[y:y2, x:x2]

    @property
    def dominant_color(self, number_of_colors=5):
        pixels = np.float32(self.image.reshape(-1, 3))

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        flags = cv2.KMEANS_RANDOM_CENTERS

        _, labels, palette = cv2.kmeans(pixels, number_of_colors, None, criteria, 10, flags)
        _, counts = np.unique(labels, return_counts=True)

        return RGBColor(palette[np.argmax(counts)])


if __name__ == '__main__':
    p = 'C:\\Users\\James\\Documents\\_Github-Projects\\bot_utils\\examples\\albion_online\\temp-pic-input.png'
    p = 'C:\\Users\\James\\Documents\\_Github-Projects\\bot_utils\\examples\\albion_online\\temp-pic-input.png'
    i = ImageAnalytics(p)
    print(i.dominant_color)
