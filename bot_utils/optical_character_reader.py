from PIL import Image
import sys

import pyocr
import pyocr.builders


class OpticalCharacterReader:
    def __init__(self):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            raise Exception("No OCR tool found; install libtesseract, tesseract, or cuneiform")
        # The tools are returned in the recommended order of usage
        self.tool = tools[0]
        # Ex: Will use tool 'libtesseract'

    def image_to_string(self, img_path, only_search_for_digits=False):
        # there's also WordBoxBuilder and LineBoxBuilder
        builder = pyocr.builders.DigitBuilder if only_search_for_digits else pyocr.builders.TextBuilder

        text = self.tool.image_to_string(
            Image.open(img_path),
            builder=builder
        )

        return text


if __name__ == '__main__':
    import os
    print(os.environ.get('TESSERACT_CMD'))
    ocr = OpticalCharacterReader()