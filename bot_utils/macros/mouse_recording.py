from os.path import join, dirname, basename
import json

from bot_utils import package_name, logger
from bot_utils.utils.serializable_interface import SerializableInterface


class MouseRecording(SerializableInterface, list):
    def __init__(self, *args, **kwargs):
        self.file_path = join(dirname(__file__), f'{package_name}_{self.__class__.__name__}_save.json')
        super().__init__(*args, **kwargs)

    def serialize(self):
        with open(self.file_path, 'w') as file:
            json.dump(self, file)  # tuples get converted to list
            return self.file_path

    @staticmethod
    def deserialize(file_path):
        try:
            with open(file_path, 'r') as file:
                recording = json.load(file)
                return MouseRecording([tuple(r) for r in recording])
        except FileNotFoundError:
            logger.warning(f'file not found: {file_path}')
            return MouseRecording()
