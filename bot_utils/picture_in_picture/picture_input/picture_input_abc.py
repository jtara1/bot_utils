import os

from bot_utils.utils import DebugAbstractClass


class PictureInputAbstractClass(DebugAbstractClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.img_path = None

    def get_image(self, img_path):
        self.img_path = img_path

    def clean(self):
        if self.img_path:
            os.remove(self.img_path)
