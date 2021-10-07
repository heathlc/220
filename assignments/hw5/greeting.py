"""
Name: Lydia Heath
greeting.py

Problem: Displaying a greeting

Certificate of Authenticity:
I certify this project is entirely my own.
"""


from time import sleep

from graphics import GraphWin, Circle, Point, Polygon, Line, Text


def main():
    win = GraphWin("Greeting", 500, 500)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("light pink")

    top_left = Circle(Point(4.3, 5.5), 0.75)
    top_left.setFill("red")
    top_left.setOutline("red")
    top_left.draw(win)

    top_right = Circle(Point(5.7, 5.5), 0.75)
    top_right.setFill("red")
    top_right.setOutline("red")
    top_right.draw(win)

    body = Polygon(Point(3.55, 5.5), Point(6.4, 5.5), Point(5, 3.2))
    body.setFill("red")
    body.setOutline("red")
    body.draw(win)

    left_line = Line(Point(3.67, 5.2), Point(5, 3.3))
    left_line.setOutline("red")
    left_line.setWidth(6)
    left_line.draw(win)

    right_line = Line(Point(6.35, 5.2), Point(5, 3.3))
    right_line.setOutline("red")
    right_line.setWidth(6)
    right_line.draw(win)

    happy_text = Text(Point(5, 9), "Happy")
    happy_text.setFill("white")
    happy_text.setSize(25)

    val_text = Text(Point(5, 8.2), "Valentine's")
    val_text.setFill("hot pink")
    val_text.setSize(30)

    day_text = Text(Point(5, 7.5), "Day!")
    day_text.setFill("white")
    day_text.setSize(25)

    happy_text.draw(win)
    sleep(0.5)
    val_text.draw(win)
    sleep(0.5)
    day_text.draw(win)
    sleep(0.5)

    arrow_head = Polygon(Point(7, 2.3), Point(7, 2.6), Point(7.3, 2.6))
    arrow_head.setFill("black")
    arrow_head.setOutline("black")
    arrow_head.draw(win)

    arrow_body = Line(Point(7.1, 2.5), Point(10, 0))
    arrow_body.setOutline("black")
    arrow_body.setWidth(4)
    arrow_body.draw(win)

    for _ in range(8):
        arrow_head.move(-0.45, 0.45)
        arrow_body.move(-0.45, 0.45)
        sleep(0.5)

    close_message = Text(Point(5, 1), "Click anywhere to close")
    close_message.setFill("white")
    close_message.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
