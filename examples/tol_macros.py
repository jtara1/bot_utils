import keyboard
import time
import mouse
import click

from bot_utils.macro import Macro


class Pickup(Macro):
    def __init__(self, hotkey='F2'):
        """
        Presses f repeatedly which picks up loot
        in a certain online game
        """
        super(Pickup, self).__init__(hotkey=hotkey)
        
    def do_action(self):
        keyboard.press_and_release('f')


class Digger(Macro):
    def __init__(self, hotkey='F3'):
        """
        Digs dirt in a certain online game
        """
        super(Digger, self).__init__(hotkey=hotkey)

    def do_action(self):
        mouse.press(button='right')
        time.sleep(0.1)
        mouse.move(-700, 0, absolute=False, duration=0.1)
        mouse.release(button='right')
        time.sleep(3)  # approx time to dig in game


class Walker(Macro):
    def __init__(self, hotkey='F4'):
        """
        Walks forward until disabled
        """
        super(Walker, self).__init__(hotkey=hotkey)

    def do_action(self):
        if self.enabled:
            keyboard.press('w')
        else:
            keyboard.release('w')

    def _run_repeatedly(self):
        """Don't need to do this for this macro"""
        pass

    def toggle_enabled(self):
        super().toggle_enabled()
        self.do_action()
    

@click.command()
@click.option('-p', '--pickup', is_flag=True, default=True,
              help='Disables pickup macro')
@click.option('-d', '--digger', is_flag=True, default=True,
              help='Disables digger macro')
@click.option('-w', '--walker', is_flag=True, default=True,
              help='Disables walker macro')
def main(pickup, digger, walker):

    def stop_all():
        for macro in macros:
            macro.stop()
    
    macros = []
    if pickup:
        macros.append(Pickup())
    if digger:
        # if digger enabled, it's best if pickup is also enabled
        macros.append(Digger())
    if walker:
        macros.append(Walker())

    # block until program exit (KeyBoardInterrupt) ctrl+c
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            stop_all()
            exit(0)


if __name__ == "__main__":
    # start the program
    main()

