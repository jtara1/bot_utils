from time import sleep
import math

import mouse

from bot_utils.macro import Macro


class AutoClicker(Macro):
    def __init__(self, click_period=1, hotkey='f2'):
        super().__init__(hotkey)
        self.action_delay = 0
        self.click_period = click_period

    def do_action(self):
        mouse.click('left')
        sleep(self.click_period)


if __name__ == '__main__':
    clicker = AutoClicker()