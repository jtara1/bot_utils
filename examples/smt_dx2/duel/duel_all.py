from time import sleep, time

from duel import duel
from bot_utils import click, double_click as doubleClick
from examples.smt_dx2.images.paths import Images

# constants
duel_prep_load = 4
duel_load = 24 + 13  # 22s to load 13s for enemy turn
duel_end = 15
duel_end_results = 4


def duel_next():
    # load
    click(Images.duel)
    sleep(duel_prep_load)
    click(Images.start_duel)
    sleep(duel_load)

    # fight
    try:
        duel()
    except:
        print('duel seems to have ended')

    # exit to duel select lobby
    sleep(duel_end)
    for i in range(3):
        click(Images.next)
        sleep(duel_end_results)


def duel_all(timeout=600):
    """duel all"""
    while True:
        print('finding next to duel')
        duel_next()


if __name__ == '__main__':
    sleep(2)
    duel_all()