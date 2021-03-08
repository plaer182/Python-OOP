#!/usr/bin/env python3
"""
    Создать класс Rectangle который конструируется с двумя аргументами height и width.
    Следует имплементировать на Rectangle следующие методы:
    ○ area() - возвращает площадь
    ○ perimeter() - возвращает периметр
    ○ __str__()
    ○ класс метод clone() - создает копию текущего объекта и возвращает
    новый объект
"""


class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def area(self):
        area = self._height * self._width
        return area

    @property
    def perimeter(self):
        perimeter = (self._height + self._width) * 2
        return perimeter

    def __str__(self):
        return "The area is: " + str(self.area) + "\n" + "The perimeter is: " + str(self.perimeter)

    @classmethod
    def clone(cls, obj):
        return cls(height=obj.height, width=obj.width)


if __name__ == '__main__':
    rectangle1 = Rectangle(height=10, width=15)
    print(rectangle1)
    print(rectangle1.perimeter)
    print(rectangle1.area)
