class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self, weight=25, thickness=5):
        return f'Масса асфальта равна: {(self._length * self._width * weight * thickness) / 1000}'


road_1 = Road(5000, 20)
print(road_1.calc())
