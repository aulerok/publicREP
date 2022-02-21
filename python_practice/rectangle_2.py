from rectangle import Rectangle, Square, Circle
# Далее создаем два прямоугольника.
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# Вывод площадей двух прямоугольников
print(f"Площадь первого прямоугольника = {rect_1.getArea()}")
print(f"Площадь второго прямоугольника = {rect_2.getArea()}")

square_1 = Square(5)
square_2 = Square(10)
print(f"Площадь первого квадрата = {square_1.getArea_square()}")
print(f"Площадь второго квадрата = {square_2.getArea_square()}")

figures = [rect_1, rect_2, square_1, square_2]
# for figure in figures:
   # if isinstance(figure, Square):
   #     print(f"{figure.getArea_square()}")
   # else:
   #     print(f"{figure.getArea()}")
circle_1 = Circle(5)
circle_2 = Circle(13)
print(f"Площадь первого круга = {circle_1.getArea_circle()} "
      f"а второго круга = {circle_2.getArea_circle()}")
figures.append(circle_1)
figures.append(circle_2)
