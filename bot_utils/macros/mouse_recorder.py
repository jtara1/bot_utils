from time import sleep, time

import mouse

from bot_utils import logger
from bot_utils.macros import MacroAbstractClass, MouseRecording


class MouseRecorder(MacroAbstractClass):
    def __init__(self, hotkey='f2'):
        self.terminate_mouse_recording_hotkey = mouse.MIDDLE

        self.mouse_recording = None
        super().__init__(hotkey)

    def do_action(self):
        # has to be a mouse hotkey to stop mouse recording
        recording = mouse.record(self.terminate_mouse_recording_hotkey, target_types=('up',))
        self.mouse_recording = MouseRecording(recording)

    def toggle_enabled(self):
        super().toggle_enabled()
        if not self.enabled:
            self.stop()
            mouse.click(self.terminate_mouse_recording_hotkey)
            sleep(3)
            self.mouse_recording.serialize()


if __name__ == '__main__':
    r = MouseRecorder()
