from figureclasses import Triangle, Cube, Rectangle
triangle_1 = Triangle(0, 0, 0, 3, 4, 5, 3,)
triangle_2 = Triangle(10, 10, 10, 5, 9, 12, 9)
print(f"площадь треугольника {triangle_1.data_triangle()} = {triangle_1.getArea_triangle()}")
print(f"площадь треугольника {triangle_2.data_triangle()} = {triangle_2.getArea_triangle()}")

cube_1 = Cube(5, 6, 10, 1)
cube_2 = Cube(-5, -6, -10, 5)
print(f"\nОбъем куба {cube_1.data_cube()} равен {cube_1.getVolume()}")
print(f"Объем куба {cube_2.data_cube()} равен {cube_2.getVolume()}")

rect_1 = Rectangle(3, 4, 5, 4, 4)
rect_2 = Rectangle(10, 11, 12, 13, 14)
print(f"\nПлощадь треугольника{rect_1.data_rect()} равна {rect_1.getArea_rect()}")
print(f"Площадь треугольника{rect_2.data_rect()} равна {rect_2.getArea_rect()}")
