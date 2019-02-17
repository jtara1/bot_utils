from bot_utils.picture_in_picture.picture_input import PictureInputAbstractClass


class LoadImage(PictureInputAbstractClass):
    def __init__(self, always_load_this_image_path=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.always_load_this_image_path = always_load_this_image_path

    def get_image(self, img_path):
        return self.always_load_this_image_path or img_path

    def clean(self):
        pass
