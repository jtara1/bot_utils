from time import time, sleep
from os.path import basename, dirname, join
import asyncio

import mouse

from bot_utils import logger
from bot_utils import PictureInPicture

from examples.smt_dx2.images import Images


async def clear_all_stages():
    logger.info(f'start HP: {clear_all_stages.__name__}')
    picture = PictureInPicture(image_similarity_threshold=.90)
    stages = [Images.one, Images.two, Images.three, Images.four, Images.five, Images.six, Images.seven, Images.eight, Images.nine, Images.ten]

    for img_path in stages:
        if '007' in basename(img_path):  # scroll down to see stages below (8 - 10)
            logger.debug('scrolling down in HP stage view')
            lower_region = picture.get_regions(Images.five)[0]
            upper_region = picture.get_regions(Images.one)[0]
            mouse.drag(*lower_region.center, *upper_region.center, duration=1)

        logger.debug(f'clicking on {img_path} asap')
        await picture.click_asap(img_path)
        await picture.click_asap(Images.enter)
        # await picture.click_asap(Images.auto_on, timeout=11)

        logger.debug('clicking on next ui asap')
        # next, next, close, next
        await picture.click_asap(Images.next)
        sleep(4)
        await picture.click_asap(Images.next)
        await picture.click_asap(Images.close, timeout=4)
        await picture.click_asap(Images.next)


if __name__ == '__main__':
    logger.info('begin')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(clear_all_stages())