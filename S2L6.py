class Road:
    _width = None
    _length = None

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class Formula(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


My_road = Formula(18, 52630, 452)
print(My_road.mass())