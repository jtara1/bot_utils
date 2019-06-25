from time import sleep

import mouse
import keyboard

from bot_utils import logger
from bot_utils.macro import Macro


class MacroRecorder(Macro):
    def __init__(self, hotkey='f2'):
        super().__init__(hotkey)

        self.terminate_mouse_recording_hotkey = mouse.MIDDLE

        self.mouse_recording = None
        self.keyboard_recording = None

    def do_action(self):
        # has to be a mouse hotkey to stop mouse recording
        self.mouse_recording = mouse.record(self.terminate_mouse_recording_hotkey)
        self.keyboard_recording = keyboard.record(until=self.hotkey)

    def stop(self):
        super().stop()
        mouse.press(self.terminate_mouse_recording_hotkey)
        logger.info('stopped recording')


if __name__ == '__main__':
    # TODO: rm, and add as test
    r = MacroRecorder()
    r.start()
    print()
