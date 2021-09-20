"""
Name: Lydia Heath
lab4.py
"""

from graphics import *

import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(200, 200), Point(180, 180))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of square

        # move amount is distance from center of square to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        sq = shape.clone()
        sq.move(dx, dy)
        sq.draw(win)

    close_pt = Point(200, 50)
    close = Text(close_pt, "Click again to quit")
    close.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    window = GraphWin("Rectangle", 400, 400)
    message = Text(Point(200, 50), "Click on two points")
    message.draw(window)

    p1 = window.getMouse()
    p1.draw(window)
    p2 = window.getMouse()
    p2.draw(window)

    rec = Rectangle(p1, p2)
    rec.setFill("blue")
    rec.draw(window)

    ln = abs(p2.getY() - p1.getY())
    w = abs(p2.getX() - p1.getX())
    perimeter = 2 * (ln + w)
    area = ln * w
    per = Text(Point(100, 350), "Perimeter: " + str(perimeter))
    ar = Text(Point(300, 350), "Area: " + str(area))
    per.draw(window)
    ar.draw(window)

    message.setText("Click again to quit")
    window.getMouse()
    window.close()


def circle():
    win = GraphWin("Circle", 400, 400)
    message = Text(Point(200, 50), "Click on a point to set the center")
    message.draw(win)

    center_pt = win.getMouse()
    center_pt.draw(win)

    message.setText("Click on another point to draw the circle")

    circumference = win.getMouse()
    circumference.draw(win)

    x = center_pt.getX() - circumference.getX()
    y = center_pt.getY() - circumference.getY()
    radius = math.sqrt((x**2) + (y**2))

    cir = Circle(center_pt, radius)
    cir.setFill("green")
    cir.draw(win)
    rad = Text(Point(200, 350), "radius: " + str(radius))
    rad.draw(win)

    message.setText("Click again to close")
    win.getMouse()
    win.close()


def pi2():
    n = eval(input("Enter in number of terms: "))
    acc = 0
    for i in range(n):
        num = 4
        denom = 1 + (2 * i)
        f = (num/denom) * ((-1)**i)
        acc = acc + f
    print("Sum =", acc)
    print("Accuracy from pi: ", math.pi - acc)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
