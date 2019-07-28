from time import sleep, time

import mouse

from bot_utils import logger
from bot_utils.macros.macro import Macro


class MacroRecorder(Macro):
    def __init__(self, hotkey='f2'):
        self.terminate_mouse_recording_hotkey = mouse.MIDDLE

        self.mouse_recording = None
        self.keyboard_recording = None
        super().__init__(hotkey)

    def do_action(self):
        # has to be a mouse hotkey to stop mouse recording
        if not self.enabled:
            self.mouse_recording = mouse.record(self.terminate_mouse_recording_hotkey)

    def toggle_enabled(self):
        if self.enabled:
            mouse.press(self.terminate_mouse_recording_hotkey)
            self.stop()
            sleep(2)
        super().toggle_enabled()


if __name__ == '__main__':
    # TODO: rm, and add as test
    recording = [mouse._mouse_event.MoveEvent(1, 1, time())]
    mouse.play(recording)
    exit()
    r = MacroRecorder()
    while not r._stop_event.wait(120):
        pass
    logger.debug('stop event fired')
    mouse.play(r.mouse_recording, speed_factor=1.1)

