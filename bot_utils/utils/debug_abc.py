import os


class DebugAbstractClass:
    def __init__(self, debug=False):
        self.debug = os.environ.get('LOGGING_LEVEL') == 'debug' or os.getenv('DEBUG') == 'true' or debug
