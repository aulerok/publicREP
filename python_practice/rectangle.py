class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea(self):
        return self.a * self.b
class Square:
    def __init__(self, a):
        self.a = a

    def getArea_square(self):
        return self.a ** 2
# Возведение в квадрат

class Circle:
    def __init__(self, a):
        self.a = a
    def getArea_circle(self):
        return self.a ** 2 * 3.14
