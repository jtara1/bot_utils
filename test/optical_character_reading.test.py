import os
import unittest

from bot_utils.optical_character_reader import OpticalCharacterReader


class TestOcr(unittest.TestCase):
    """test OCR class"""
    def test_region(self):
        img_path = os.path.join(__file__, '..', 'images', 'hp and mp.PNG')
        img_path2 = os.path.join(__file__, '..', 'images', 'hp and mp - rotated.PNG')
        ocr = OpticalCharacterReader()
        print(ocr.image_to_string(img_path, True))
        print(ocr.image_to_string(img_path2, True))


if __name__ == '__main__':
    unittest.main()
