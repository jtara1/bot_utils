import keyboard
from time import sleep

import mouse

from bot_utils.picture_in_picture.picture_in_picture import PictureInPicture
from bot_utils import logger

from examples.albion_online.images import Images


pip = PictureInPicture()


async def run():
    # click herb to pick up 9 times
    for i in range(2):
        # click on herb
        await pip.click_asap(Images.t8_herb)

        # click take
        await pip.click_asap(Images.take)
        sleep(3)

        # mount up
        logger.debug('mounting up')
        mouse.move(1281, 603) # char in center for albion for 1440p
        mouse.click()

    # while True:
    #     r = pip.get_regions(Images.t8_herb)
    #     print(r)
    #     # sleep(3)
    #     return
    #     # await pip.click_asap(Images.take_all)


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()

    async def start():
        await run()

    loop.run_until_complete(start())
