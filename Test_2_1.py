class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_rectanle(self):
        return str(self.x), str(self.y), str(self.width), str(self.height)

    def get_area(self):
        return self.x*self.y

