import sys
from os.path import join, dirname
from time import time
from loguru import logger


version = '0.0.1'
package_name = 'bot_utils'
module_dir = join(dirname(__file__))
logs_dir = join(module_dir, 'logs')  # loguru doesn't actually serialize logs locally
session_dir = join(module_dir, str(time()))
is_mac_os = sys.platform == 'darwin'

if not is_mac_os:
    from bot_utils.deprecated.deprecated_click_functions import click, double_click
    from bot_utils.picture_in_picture import PictureInPicture
