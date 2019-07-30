from os.path import join, dirname, basename
import json

import mouse
from mouse._mouse_event import MoveEvent, ButtonEvent, WheelEvent

from bot_utils import package_name, logger
from bot_utils.utils.serializable_interface import SerializableInterface


class MouseRecording(SerializableInterface, list):
    save_file = join(dirname(__file__), f'{package_name}_MouseRecording_save.json')

    def __init__(self, *args, **kwargs):
        self.file_path = MouseRecording.save_file
        super().__init__(*args, **kwargs)

    def serialize(self):
        with open(self.file_path, 'w') as file:
            json.dump(self, file)  # tuples get converted to list
            return self.file_path

    @staticmethod
    def deserialize(file_path=None):
        path = file_path or MouseRecording.save_file

        try:
            with open(path, 'r') as file:
                recording = json.load(file)
                return MouseRecording([MouseRecording.convert_tuple_to_event_tuple(r) for r in recording])
        except FileNotFoundError:
            logger.warning(f'file not found: {path}')
            return MouseRecording()

    @staticmethod
    def convert_tuple_to_event_tuple(sequence):
        if len(sequence) == 2:
            return WheelEvent(*sequence)
        elif isinstance(sequence[0], str):
            return ButtonEvent(*sequence)
        return MoveEvent(*sequence)
