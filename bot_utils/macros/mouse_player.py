import mouse

from bot_utils import logger
from bot_utils.macros import MacroAbstractClass, MouseRecording


class MousePlayer(MacroAbstractClass):
    def __init__(self, hotkey='f2'):
        self.mouse_recording = MouseRecording.deserialize()
        super().__init__(hotkey)

    def do_action(self):
        mouse.play(self.mouse_recording, speed_factor=1.05)
        self.set_enabled(False)


if __name__ == '__main__':
    r = MousePlayer()

