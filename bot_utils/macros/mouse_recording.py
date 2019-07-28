import mouse
import tempfile
import json

from bot_utils import package_name, logger
from bot_utils.utils.serializable_interface import SerializableInterface


class MouseRecording(SerializableInterface, list):
    def __init__(self, *args, **kwargs):
        self.file = tempfile.NamedTemporaryFile(mode='w+', prefix=f'{package_name}_', encoding='utf-8')
        super().__init__(*args, **kwargs)

    @property
    def file_path(self):
        return self.file.name

    def serialize(self):
        valid_json = [list(value) for value in self]
        json.dump(valid_json, self.file)
        return self.file_path

    @staticmethod
    def deserialize(file_path):
        try:
            recording = json.load(file_path)
            return MouseRecording(recording)
        except:
            logger.warning(f'file not found: {file_path}')
            return MouseRecording()
