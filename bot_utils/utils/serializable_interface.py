class SerializableInterface:
    def serialize(self):
        raise Exception('not implemented')

    @staticmethod
    def deserialize(file_path):
        raise Exception('not implemented')
