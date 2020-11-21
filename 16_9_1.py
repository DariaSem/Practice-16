from figures_16_9_1 import Rectangle, Triangle, Square, Circle

rect_1 = Rectangle(5, 10, 50, 100)
print('Ширина прямоугольника =', rect_1.get_width())
print('Площадь прямоугольника =', rect_1.get_area())

triangle_1 = Triangle(6, 10)
print('Площадь треугольника =', triangle_1.get_area())

square_1 = Square(7)
print('Сторона квадрата =', square_1.get_height())
print('Площадь квадрата =', square_1.get_area())

circle_1 = Circle(3.9)
print('Радиус окружности =', circle_1.get_rad())
print('Площадь круга =', circle_1.get_area())