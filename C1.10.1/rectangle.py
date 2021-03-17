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

    def set_x(self, x):
        if isinstance(x, int) or isinstance(x, float):
            self.x = x
            return True
        return False

    def set_y(self, y):
        if isinstance(y, int) or isinstance(y, float):
            self.y = y
            return True
        return False

    def set_width(self, width):
        if (isinstance(width, int) or isinstance(width, float)) and width >= 0:
            self.width = width
            return True
        return False

    def set_height(self, height):
        if (isinstance(height, int) or isinstance(height, float)) and height >= 0:
            self.height = height
            return True
        return False

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        _ = (str(self.x), str(self.y), str(self.width), str(self.height))
        return "Rectangle (" + ", ".join(_) + ")"


class Square:
    def __init__(self, x, y, a):
        self.a = a
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_a(self):
        return self.a

    def set_x(self, x):
        if isinstance(x, int) or isinstance(x, float):
            self.x = x
            return True
        return False

    def set_y(self, y):
        if isinstance(y, int) or isinstance(y, float):
            self.y = y
            return True
        return False

    def set_a(self, a):
        if (isinstance(a, int) or isinstance(a, float)) and a >= 0:
            self.a = a
            return True
        return False

    def get_area_square(self):
        return self.a ** 2

    def __str__(self):
        _ = (str(self.x), str(self.y), str(self.a))
        return "Square (" + ", ".join(_) + ")"


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_radius(self):
        return self.radius

    def set_x(self, x):
        if isinstance(x, int) or isinstance(x, float):
            self.x = x
            return True
        return False

    def set_y(self, y):
        if isinstance(y, int) or isinstance(y, float):
            self.y = y
            return True
        return False

    def set_radius(self, radius):
        if (isinstance(radius, int) or isinstance(radius, float)) and radius >= 0:
            self.radius = radius
            return True
        return False

    def get_area_circle(self):
        return 3.14 * self.radius ** 2

    def __str__(self):
        return "Circle (" + str(self.radius) + ")"