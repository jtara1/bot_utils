import keyboard

from bot_utils.picture_in_picture.picture_in_picture import PictureInPicture

from examples.albion_online.images import Images


pip = PictureInPicture()


async def take_journal():
    await pip.click_asap(Images.take_all)


async def give_journal(journal_img):
    keyboard.press('shift')
    try:
        await pip.click_asap(journal_img)
    except Exception as exception:
        raise exception
    finally:
        keyboard.release('shift')

    await pip.click_asap(Images.accept)


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()

    async def start():
        await take_journal()
        await give_journal(Images.t6_fletcher_journal)

    loop.run_until_complete(start())
