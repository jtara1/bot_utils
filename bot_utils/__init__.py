import sys

is_macos = sys.platform == 'darwin'

from jtara1_util import setup_logger
# logger = setup_logger('bot_utils')

class PrintLogger:
    def __init__(self):
        self.stdout = print

    def info(self, msg, *args):
        self.stdout(msg, *args)

    def debug(self, msg, *args):
        self.stdout(msg, *args)

logger = PrintLogger()

if not is_macos:
    from bot_utils.deprecated.deprecated_click_functions import click, double_click
    from bot_utils.picture_in_picture import PictureInPicture

