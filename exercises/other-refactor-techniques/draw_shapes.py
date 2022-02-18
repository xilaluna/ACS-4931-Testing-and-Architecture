# by Kami Bigdely
# Extract superclass.

class Shape:
    def __init__(self, name, x, y, visible=True):
        self.name = name
        self.x = x
        self.y = y
        self.visible = visible

    def display(self):
        if self.visible:
            print(f'drew the {self.name}')

    def set_visibility(self, is_visible):
        self.visible = is_visible

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True


class Circle(Shape):

    def __init__(self, x, y, r, visible=True):
        super().__init__("Circle", x, y, visible)
        self.r = r

    def get_center(self):
        return self.x, self.y


class Rectangle(Shape):

    def __init__(self, x, y, width, height, visible=True):
        super().__init__("Rectangle", x, y, visible)
        self.width = width
        self.height = height

    def get_center(self):
        return self.x + self.width/2, \
            self.y + self.height/2


if __name__ == "__main__":
    circle = Circle(0, 0, 10, False)
    circle.set_visibility(True)
    circle.display()
    print('center point', circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display()  # does not display because it's hidden.
    rect.show()
    rect.display()
    print('center point', rect.get_center())
