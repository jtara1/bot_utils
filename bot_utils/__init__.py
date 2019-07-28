import sys
from loguru import logger


version = '0.0.1'
package_name = 'bot_utils'
is_mac_os = sys.platform == 'darwin'

if not is_mac_os:
    from bot_utils.deprecated.deprecated_click_functions import click, double_click
    from bot_utils.picture_in_picture import PictureInPicture
