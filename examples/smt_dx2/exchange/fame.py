from time import sleep

from bot_utils import click
from examples.smt_dx2.images import Images


# constants
class Time:
    ui_load = 1.2
    processed = 1.8


def get_summon_files(amount=1):
    for i in range(amount):
        sleep(0.1)
        click(Images.exchange_100)
        sleep(Time.ui_load)
        click(Images.exchange_100)

        sleep(Time.ui_load)
        click(Images.close)

        sleep(Time.processed)


if __name__ == '__main__':
    get_summon_files(20)
