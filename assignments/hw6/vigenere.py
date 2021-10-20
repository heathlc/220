"""
Name: Lydia Heath
vigenere.py

Problem: Create a GUI and implement a vigenere cipher.

Certificate of Authenticity:
I certify this work is entirely my own.
"""

from graphics import *


def code(message, keyword):
    message = "".join(message.split(" "))
    message_cap = message.upper()
    keyword_cap = keyword.upper()
    key = keyword_cap * 16
    acc = ""
    for i in range(len(message_cap)):
        c = ord(message_cap[i])
        ck = ord(key[i])
        char = c + ck - 91
        if char <= 64:
            new_char = chr(char + 26)
        else:
            new_char = chr(char)
        acc = acc + new_char
    return acc


def main():
    win = GraphWin("Vigenere", 500, 400)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("light grey")

    message_input = Entry(Point(6, 8), 25)
    message_input.draw(win)

    message_text = Text(Point(2.7, 8), "Message to code")
    message_text.setSize(14)
    message_text.draw(win)

    key_input = Entry(Point(5.3, 7), 15)
    key_input.draw(win)

    key_text = Text(Point(2.85, 7), "Enter Keyword")
    key_text.setSize(14)
    key_text.draw(win)

    button_text = Text(Point(5.18, 5.5), "Encode")
    button_text.setSize(14)
    button = Rectangle(Point(4.18, 6), Point(6.18, 5))
    button_text.draw(win)
    button.draw(win)

    win.getMouse()
    button.undraw()
    button_text.undraw()

    result = Text(Point(5.18, 4), "Resulting Message")
    result.draw(win)
    result_message = Text(Point(5.18, 3.5), code(message_input.getText(), key_input.getText()))
    result_message.draw(win)
    close_message = Text(Point(5.18, 1), "Click anywhere to close")
    close_message.draw(win)

    win.getMouse()


if __name__ == '__main__':
    main()
