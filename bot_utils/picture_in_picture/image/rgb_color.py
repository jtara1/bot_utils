class RGBColor(list):
    @property
    def dominant_channel(self):
        if max(self) == self[0]:
            return 'red'
        if max(self) == self[1]:
            return 'green'
        if max(self) == self[2]:
            return 'blue'