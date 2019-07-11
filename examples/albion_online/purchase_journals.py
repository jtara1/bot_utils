import asyncio
from time import sleep

import click
from loguru import logger

from bot_utils.picture_in_picture import PictureInPicture
from examples.albion_online.images import Images


@click.command()
@click.option('--amount', default=10)
async def main(amount):
    for i in range(amount):
        await purchase_a_journal()
    logger.verbose('purchased all journals', {'amount': amount})


async def purchase_a_journal():
    pip = PictureInPicture()
    await pip.click_asap(Images.buy)
    await pip.click_asap(Images.pay)
    logger.verbose('purchased a journal')


if __name__ == '__main__':
    sleep(1.5)
    logger.info('begin')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main)
