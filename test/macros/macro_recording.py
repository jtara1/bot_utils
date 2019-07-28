import unittest
from time import time

from bot_utils.macros.mouse_recording import MouseRecording


class TestMouseRecording(unittest.TestCase):
    """test picture in picture class"""
    def test_mouse_recording(self):
        recording = MouseRecording(
            [(1, 1, time()), (500, 500, time())],
        )

        path = recording.serialize()
        recording2 = MouseRecording.deserialize(path)
        self.assertEqual(recording, recording2)


if __name__ == '__main__':
    unittest.main()