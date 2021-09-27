"""
Name: Lydia Heath
lab5.py
"""

from graphics import *


import math


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    white_r = win_width / 2
    white_cir = Circle(Point(250, 250), white_r)
    white_cir.setFill("white")
    white_cir.draw(win)
    r = white_r / 5
    black_cir = Circle(Point(250, 250), r * 4)
    black_cir.setFill("black")
    black_cir.draw(win)
    blue_cir = Circle(Point(250, 250), r * 3)
    blue_cir.setFill("blue")
    blue_cir.draw(win)
    red_cir = Circle(Point(250, 250), r * 2)
    red_cir.setFill("red")
    red_cir.draw(win)
    yellow_cir = Circle(Point(250, 250), r)
    yellow_cir.setFill("yellow")
    yellow_cir.draw(win)

    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    s1 = Line(p1, p2)
    s1.draw(win)
    s2 = Line(p2, p3)
    s2.draw(win)
    s3 = Line(p3, p1)
    s3.draw(win)

    ax = p2.getX() - p1.getX()
    ay = p2.getY() - p1.getY()
    length_a = math.sqrt((ax**2) + (ay**2))
    bx = p3.getX() - p2.getX()
    by = p3.getY() - p2.getY()
    length_b = math.sqrt((bx**2) + (by**2))
    cx = p1.getX() - p3.getX()
    cy = p1.getY() - p3.getY()
    length_c = math.sqrt((cx**2) + (cy**2))
    perimeter = length_a + length_b + length_c
    s = perimeter / 2
    area = math.sqrt(s * (s - length_a) * (s - length_b) * (s - length_c))

    perimeter_text = Text(Point(150, 450), "Perimeter = " + str(perimeter))
    perimeter_text.draw(win)
    area_text = Text(Point(350, 450), "Area = " + str(area))
    area_text.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry = Entry(Point(win_width / 2 - 10, win_height / 2 + 40), 3)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry = red_entry.clone()
    green_entry.move(0, 30)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry = red_entry.clone()
    blue_entry.move(0, 60)

    # display rgb text
    red_text.draw(win)
    red_entry.draw(win)
    green_text.draw(win)
    green_entry.draw(win)
    blue_text.draw(win)
    blue_entry.draw(win)

    win.getMouse()

    for i in range(5):
        r = int(red_entry.getText())
        g = int(green_entry.getText())
        b = int(blue_entry.getText())
        color = color_rgb(r, g, b)
        shape.setFill(color)
        win.getMouse()

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = input("Enter a string: ")
    first_ch = string[0]
    print(first_ch)
    last_ch = string[-1]
    print(last_ch)
    middle_chs = string[2:6]
    print(middle_chs)
    concat = string[0] + string[-1]
    print(concat)
    rep = string[0:3] * 10
    print(rep)
    for c in string:
        print(c)
    print(len(string))


def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[-1])]
    print(x)
    x = values[2] + values[0] + float(values[-1])
    print(x)
    x = len(values)
    print(x)


def another_series():
    n = eval(input("Enter number of terms: "))
    acc = 0
    for i in range(n):
        y = 2 + (2 * (i % 3))
        print(y, end=" ")
        acc = acc + y
    print(acc)


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    pass


main()
