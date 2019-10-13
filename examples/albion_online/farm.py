from time import sleep

import keyboard
import mouse

from bot_utils.picture_in_picture.picture_in_picture import PictureInPicture
from bot_utils.picture_in_picture.picture_input import Screenshot
from bot_utils.picture_in_picture.image.image_analytics import ImageAnalytics
from bot_utils import logger

from examples.albion_online.images import Images


pip = PictureInPicture()


async def run():
    # click herb to pick up 9 times
    for i in range(7):
        # click on herb
        region = await pip.click_asap(Images.t8_herb, timeout=5)
        if not region:
            logger.info('no herb')
            continue

        # click take ui
        region = await pip.click_asap(Images.take, timeout=5)
        if not region:
            logger.info('no take ui')
            continue

        logger.info('mounting up')
        mount_up()


def mount_up():
    crop_region = (720, 1340, 1254, 76)  # TODO: scale with non-1440p
    pip_skills = PictureInPicture(picture_input=Screenshot(crop_region=crop_region, cleanup_after=False))

    x, y, x2, y2 = pip_skills.get_regions(Images.mount_up)[0]
    relative_region = (x - crop_region[0], y - crop_region[1], x2 - crop_region[0], y2 - crop_region[1])

    rgb_color = ImageAnalytics(pip_skills.vision.picture_input.img_path, relative_region).dominant_color
    if rgb_color.dominant_channel == 'green':
        pip_skills.click(Images.mount_up)

    sleep(4.1)


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()

    async def start():
        await run()

    loop.run_until_complete(start())
