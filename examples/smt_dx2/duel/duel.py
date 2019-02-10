from time import sleep

from bot_utils import click, double_click as doubleClick
from bot_utils.decorators import ignore_exception
from bot_utils.exceptions import TemplateImageNotFound
from bot_utils.utils import unpack_methods

from examples.smt_dx2.images.paths import Images

# constants
single_attack_time = 4
enemy_turn_time = 11


class Fighter:
    """this is a singleton within this script"""
    def __init__(self, ignore_img_not_found=True):
        decorator = ignore_exception(TemplateImageNotFound)

        if ignore_img_not_found:
            # all methods
            for func in dir(self):
                # not an operator or private method
                if '__' not in func:
                    # apply the func decorator to ignore the exception
                    setattr(self, func, decorator(getattr(self, func)))

    def auto_this_turn(self):
        doubleClick(Images.auto_on)
        sleep(single_attack_time)

    def auto_on(self):
        click(Images.auto_on)
        sleep(0.05)

    def auto_off(self):
        click(Images.auto_off)
        sleep(0.05)

    def pass_now(self):
        click(Images.pass_turn)
        sleep(single_attack_time)

    def tag(self):
        click(Images.tag)
        sleep(single_attack_time)


fighter = Fighter()
unpack_methods(fighter, globals())

"""
collection of actions
"""
def turn_one():
    """pi is alias for press icon"""
    print('start turn 1')
    # trump
    click(Images.concentrate)
    sleep(single_attack_time)
    
    # fenrir, 3 pi
    auto_this_turn()
    
    # jack1, 2 pi
    tag()

    # jack2, 2 pi
    tag()
    
    # trump, 2 pi
    auto_this_turn()
    
    try:
        # fenrir, 1 pi
        pass_now()
    
        # jack 1, .5 pi
        tag()
    
        # jack 2, .5 pi
        tag()
    
        # trump
        auto_this_turn()
    except:
        print('seems to have missed an atk')

    # turn ends
    sleep(enemy_turn_time)


def generic_turn():
    print('start generic turn')
    def sub_turn_cycle():
        print('start sub-turn cycle')
        # trump 
        auto_this_turn()
    
        # fenrir, 3 pi
        pass_now()
        
        # jack1, 2.5 pi
        tag()
    
        # jack2, 2.5 pi
        tag()

    for i in range(3):
        sub_turn_cycle()

    auto_this_turn()
    sleep(enemy_turn_time)


def duel():
    turn_one()
    generic_turn()
    print('auto the rest')
    auto_on()


if __name__ == '__main__':
    """file ran directly"""
    duel()
