import os


class DebugAbstractClass:
    def __init__(self, debug=os.environ.get('LOGGING_LEVEL') == 'debug'):
        self.debug = debug
