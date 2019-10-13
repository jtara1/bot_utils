import keyboard
from time import sleep

import mouse

from bot_utils.picture_in_picture.picture_in_picture import PictureInPicture
from bot_utils.picture_in_picture.picture_input import Screenshot
from bot_utils.picture_in_picture.image.image_analytics import ImageAnalytics
from bot_utils import logger

from examples.albion_online.images import Images


pip = PictureInPicture()


async def run():
    # click herb to pick up 9 times
    for i in range(2):
        # click on herb
        await pip.click_asap(Images.t8_herb, timeout=5)

        # click take
        await pip.click_asap(Images.take, timeout=5)
        # sleep(3)

        # mount up
        logger.debug('mounting up')
        mount_up()
        # keyboard.press_and_release('a')
        # mouse.move(1290, 536) # char in center for albion for 1440p
        # mouse.click()
        # sleep(1.7)

    # while True:
    #     r = pip.get_regions(Images.t8_herb)
    #     print(r)
    #     # sleep(3)
    #     return
    #     # await pip.click_asap(Images.take_all)


def mount_up():
    crop_region = (720, 1340, 1254, 76)
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
        # await run()
        mount_up()

    loop.run_until_complete(start())
