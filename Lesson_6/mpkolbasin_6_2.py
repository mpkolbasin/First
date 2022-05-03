# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self, weight=25, thickness=5):
        return f'Total mass of asphalt: {(self._length * self._width * weight * thickness) / 1000} t.'


road_1 = Road(5000, 20)
print(road_1.calculation())
