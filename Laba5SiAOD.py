from abc import ABC, abstractmethod  # импортируем класс ABC
import math
from shapely.geometry import Polygon
from shapely import area as meme_area, length as pepe_length


class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        return meme_area(Polygon(self._coordinates))

    @property
    @abstractmethod
    def perimeter(self):
        return pepe_length(Polygon(self._coordinates))


class Triangle(Figure):
    def __init__(self, coordinates):
        if len(coordinates) != 3:
            raise FigureExceptions("треугольник должен иметь три координаты")
        for i in coordinates:
            if len(i) != 2 or any(z < 0 for z in i):
                raise FigureExceptions("координаты могут иметь только положительные значения")

        self._coordinates = coordinates
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x3, y3 = coordinates[2]
        self.a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # вычисление длины сторон треугольника по формуле
        self.b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        self.c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            raise TriangleExceptions("треугольник не может существовать в этой вселенной")

    @property
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    def bera(self):  # равнобедренный или равносторонний треугольник?
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return 'Равнобедренный треугольник'
        elif self.a == self.b == self.c:
            return 'Равносторонний треугольник'
        else:
            return 'Разносторонний треугольник'


def peresec (self, other):
    lupa = Polygon(self._coordinates)
    pupa = Polygon(other._coordinates)
    return lupa.intersects(pupa)


class Quadrilateral(Figure):
    def __init__(self, coordinates):
        if len(coordinates) != 4:
            raise FigureExceptions("четырехугольник должен иметь четыре координаты")
        for i in coordinates:
            if len(i) != 2 or any(z < 0 for z in i):
                raise FigureExceptions("координаты могут иметь только положительные значения")

        self._coordinates = coordinates
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x3, y3 = coordinates[2]
        x4, y4 = coordinates[3]
        self.a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        self.c = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        self.d = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
        kva = Polygon(self._coordinates)
        if not kva.is_valid:
            raise QuadrilateralExceptions("четырехугольник не может существовать в этой вселенной")

    @property
    def area(self):  # метод из библиотеки shapely
        kva = Polygon(self._coordinates)
        return round(meme_area(kva), 3)

    @property
    def perimeter(self):  # метод из библиотеки shapely
        kva = Polygon(self._coordinates)
        return round(pepe_length(kva), 3)

    def pr(self):
        dia1 = math.sqrt(self.a ** 2 + self.b ** 2)
        dia2 = math.sqrt(self.c ** 2 + self.d ** 2)
        if self.a == self.b and self.b == self.c and self.c == self.d:
            return 'Ромб'
        if self.a == self.c and self.b == self.d:
            return 'Параллелограмм'
        if self.a == self.c and self.b == self.d and dia1 == dia2:
            return 'Прямоугольник'

        else:
            return 'Четырехугольник'


# ошибо4ки


class FigureExceptions(Exception):
    pass


class TriangleExceptions(FigureExceptions):
    pass


class QuadrilateralExceptions(FigureExceptions):
    pass


tr1 = Quadrilateral([[1, 1], [2, 2], [3, 3], [4, 4]])
print(tr1.pr())
# лирическое отступление, я 4 дня сидела с этой лабой в силу того, что терпеть ненавижу геометрию
# как вы можете догадаться, бесподобная мама сашенька степанова вновь мне помогла советом
# могу вам любезно в случае чего скинуть переписку с ней, как я тупич пыталась понять, что делать
# изначально мой код был похож на страшный сон
# библиотека shapely вообще тема, оказывается, не пришлось изобретать велосипед
