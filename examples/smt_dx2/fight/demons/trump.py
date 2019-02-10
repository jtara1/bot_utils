import asyncio

from examples.smt_dx2.fight.demons.base_demon import BaseDemon
from examples.smt_dx2.images import Images
from bot_utils.picture_in_picture import PictureInPicture


class Trump(BaseDemon):
    def __init__(self):
        self.picture = PictureInPicture(ignore_template_not_found=True)

    async def take_turn_action(self):
        await self.picture.click_asap(Images.trump)
        if await self.picture.has_image_within_period(Images.concentrate_status):  # (something) is in concentrate state
            clicked_region = self.picture.click(Images.apocalypse)
            if not clicked_region:
                self.picture.click(Images.pass_turn)

        else:  # (nothing) is in concentrate state
            clicked_region = self.picture.click(Images.concentrate)
            if not clicked_region:
                self.picture.click(Images.pass_turn)


if __name__ == '__main__':
    # test
    async def test():
        trump = Trump()
        import time
        while True:
            await trump.take_turn_action()
            time.sleep(3)

    # asyncio.run(test())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())