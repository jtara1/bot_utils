from bot_utils.utils import DebugAbstractClass


class PictureInputInterface(DebugAbstractClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_image(self, img_path):
        raise Exception('not implemented')
