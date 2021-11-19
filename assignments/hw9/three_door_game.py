"""
Name: Lydia Heath
three_door_game.py

Purpose: Testing button class

Certificate of Authenticity:
I certify this work is entirely my own.
"""

from random import randrange
from graphics import GraphWin, Text, Point
from button import Button

"""
I updated my pytest to fit my program as I could not think of a way to change the button class constructor 
to have the rectangle shape as an instance variable compared to having the points being instance variables. 
"""


def main():
    win = GraphWin("Three Door Game", 400, 400)
    win.setCoords(0, 0, 10, 10)

    secret_door_text = Text(Point(5, 9), "I have a secret door")
    secret_door_text.draw(win)
    click_to_choose = Text(Point(5, 1), "Click to choose my secret door")
    click_to_choose.draw(win)

    button_1 = Button(Point(1, 4), Point(3, 6), "Door One")
    button_1.draw(win)
    button_2 = Button(Point(4, 4), Point(6, 6), "Door Two")
    button_2.draw(win)
    button_3 = Button(Point(7, 4), Point(9, 6), "Door Three")
    button_3.draw(win)

    random_door = randrange(1, 4)
    clicked_point = win.getMouse()
    winning_text = Text(Point(5, 1), "You win!")
    losing_text = Text(Point(5, 1), "You lose, the secret door was door " + str(random_door))

    if random_door == 1 and button_1.is_clicked(clicked_point):
        button_1.color_button("green")
        click_to_choose.undraw()
        winning_text.draw(win)
    elif random_door == 2 and button_2.is_clicked(clicked_point):
        button_2.color_button("green")
        click_to_choose.undraw()
        winning_text.draw(win)
    elif random_door == 3 and button_3.is_clicked(clicked_point):
        button_3.color_button("green")
        click_to_choose.undraw()
        winning_text.draw(win)
    else:
        if button_1.is_clicked(clicked_point):
            button_1.color_button("red")
            click_to_choose.undraw()
            losing_text.draw(win)
        if button_2.is_clicked(clicked_point):
            button_2.color_button("red")
            click_to_choose.undraw()
            losing_text.draw(win)
        if button_3.is_clicked(clicked_point):
            button_3.color_button("red")
            click_to_choose.undraw()
            losing_text.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
