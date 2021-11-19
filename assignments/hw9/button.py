"""
Name: Lydia Heath
button.py

Purpose: Creating a user defined class and a GUI game to test it.

Certificate of Authenticity:
I certify this work is entirely my own.
"""

from graphics import Rectangle, Text, Point


class Button:
    """
    Class to build a button for three door game
    """
    def __init__(self, button_p1, button_p2, label):
        self.button = Rectangle(button_p1, button_p2)
        self.p1_x = button_p1.getX()
        self.p1_y = button_p1.getY()
        self.p2_x = button_p2.getX()
        self.p2_y = button_p2.getY()
        self.label = Text(Point((button_p2.getX() + button_p1.getX()) / 2, (button_p2.getY() + button_p1.getY()) / 2)
                          , label)

    def get_label(self):
        return self.label.getText()

    def draw(self, win):
        self.button.draw(win)
        self.label.draw(win)

    def undraw(self):
        self.button.undraw()
        self.label.undraw()

    def is_clicked(self, point):
        return self.p1_x <= point.getX() <= self.p2_x and self.p1_y <= point.getY() <= self.p2_y

    def color_button(self, color):
        self.button.setFill(color)

    def set_label(self, label):
        self.label.setText(label)
