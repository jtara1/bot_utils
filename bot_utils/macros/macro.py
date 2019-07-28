import keyboard
import time
import threading

from bot_utils import logger


class Macro(threading.Thread):
    def __init__(self, hotkey, termination_condition=lambda self: False):
        """
        Abstract class for macro
        """
        self.hotkey = hotkey
        self.enabled = False
        self.terminate = False
        self.action_delay = 0.5  # delay after action has been done
        self.actions_done_count = 0
        self.termination_condition = termination_condition

        self.thread = threading.Thread(target=self._run_repeatedly)
        self.start()
        self._stop_event = threading.Event()

        self.create_hotkey()

    def create_hotkey(self):
        keyboard.add_hotkey(
            hotkey=self.hotkey,
            callback=self.toggle_enabled)

    def start(self):
        """Start the thread which should start the loop which
        should be ready to repeatedly do some action
        """
        self.thread.start()
        logger.debug(f'{self.__class__.__name__}: started macro')

    def _run_repeatedly(self):
        """Does the action over and over again
        until it's disabled
        """
        while not self.terminate:
            while self.enabled or not self.termination_condition(self):
                # need to implement this in child class
                try:
                    self.do_action()
                    self.actions_done_count += 1
                    time.sleep(self.action_delay)
                except KeyboardInterrupt:
                    self.stop()
            time.sleep(1)

    def do_action(self):
        raise Exception("Not implemented yet")

    def toggle_enabled(self):
        self.enabled = not self.enabled
        logger.debug("{} {}".format(self.__class__.__name__, str(self.enabled)))

    def stop(self):
        """Stop the thread. We're no longer doing any action
        with any hotkeys created
        """
        self._stop_event.set()
        logger.debug(f'{self.__class__.__name__}: stopped macro')
