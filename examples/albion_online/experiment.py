import keyboard
from time import sleep

from bot_utils.picture_in_picture.picture_in_picture import PictureInPicture

from examples.albion_online.images import Images


pip = PictureInPicture()


async def run():
    while True:
        r = pip.get_regions(Images.fletcher_npc)
        print(r)
        sleep(3)
        return
        # await pip.click_asap(Images.take_all)


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()

    async def start():
        await run()

    loop.run_until_complete(start())
