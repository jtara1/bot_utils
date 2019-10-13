import os

from bot_utils.utils import DebugAbstractClass


class PictureInputAbstractClass(DebugAbstractClass):
    def __init__(self, cleanup_after=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.img_path = None
        self.cleanup_after = cleanup_after

    def get_image(self, img_path):
        self.img_path = os.path.abspath(img_path)

    def update_region(self, region):
        """if the picture input implementated class does something to offset pixels
        or change the size, we may need to know where a selected coord or region is in the origin screenshot
        or picture we searched in

        :param region:
        :return:
        """
        return region

    def clean(self):
        if self.img_path and self.cleanup_after:
            os.remove(self.img_path)
