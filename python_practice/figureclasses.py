class Triangle:
    def __init__(self, x, y, z, a, b, c, h):
        self.x = x  # координата оси х
        self.y = y  # координата оси у
        self.z = z  # координата оси z
        self.a = a  # сторона а
        self.b = b  # сторона b
        self.c = c  # сторона с (основание)
        self.h = h  # высота треугольника

    def getArea_triangle(self):  # функция вычисления площади треугольника
        return self.c * self.h / 2

    def data_triangle(self):  # функция  вывода информации о треугольнике
        return self.x, self.y, self.z, self.a, self.b, self.c, self.h


class Cube:
    def __init__(self, x, y, z, a, ):
        self.x = x
        self.y = y
        self.z = z
        self.a = a

    def getVolume(self):
        return self.a ** 3

    def data_cube(self):
        return self.x, self.y, self.z, self.a


class Rectangle:
    def __init__(self, x, y, z, a, b):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b

    def getArea_rect(self):
        return self.a * self.b

    def data_rect(self):
        return self.x, self.y, self.z, self.a, self.b
