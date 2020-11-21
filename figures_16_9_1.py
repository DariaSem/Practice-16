class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.height * self.width


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_base(self):
        return self.base

    def get_height(self):
        return self.height

    def get_area(self):
        return 0.5 * self.base * self.height


class Square:
    def __init__(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def get_area(self):
        return self.height ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def get_rad(self):
        return self.r

    def get_area(self):
        return 3.14 * self.r ** 2
