class Region(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def center(self):
        x = (self[0] + self[2]) // 2
        y = (self[1] + self[3]) // 2
        return x, y

    def add_element_wise(self, region):
        if len(region) != len(self):
            raise Exception('lengths mismatch')

        values = []
        for a, b in zip(self, region):
            values.append(a + b)

        return Region(values)