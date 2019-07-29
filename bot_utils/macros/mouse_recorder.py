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
        if not self.enabled:
            # has to be a mouse hotkey to stop mouse recording
            recording = mouse.record(self.terminate_mouse_recording_hotkey, target_types=('up',))
            self.mouse_recording = MouseRecording(recording)

    def toggle_enabled(self):
        if self.enabled:
            mouse.click(self.terminate_mouse_recording_hotkey)
            sleep(1)
            self.stop()
            self.mouse_recording.serialize()
        super().toggle_enabled()


if __name__ == '__main__':
    r = MouseRecorder()
    while not r._stop_event.wait(120):
        pass
    # mouse.play(r.mouse_recording, speed_factor=1.0)
