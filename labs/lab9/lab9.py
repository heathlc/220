"""
Name: Lydia Heath
lab9.py
"""


from graphics import *
import math


def addTens(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    return nums


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = nums[i] + acc
    return acc


def toNumbers(str_list):
    for i in range(len(str_list)):
        str_list[i] = float(str_list[i])
    return str_list


def writeSumOfSquares():
    in_file = input("enter input file name: ")
    out_file = input("enter output file name: ")
    readfile = open(in_file, 'r')
    writefile = open(out_file, 'w')
    for line in readfile:
        nums = line.split()
        list_nums = toNumbers(nums)
        square_nums = squareEach(list_nums)
        summation = round(sumList(square_nums), 1)
        writefile.write("sum of squares = " + str(summation) + "\n")


def starter():
    weight = eval(input("enter player weight: "))
    num_wins = eval(input("enter number of wins: "))
    if 150 <= weight < 160 and num_wins >= 5:
        print("player is a starter")
    elif weight > 199 or num_wins > 20:
        print("player is a starter")
    else:
        print("player is not a starter")


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


def circleOverlap():
    win = GraphWin("Circle Overlap", 400, 400)
    win.setCoords(0, 0, 10, 10)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)

    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if distance <= (r + r2):
        overlap = Text(Point(5, 1), "The circles overlap")
        overlap.draw(win)
    else:
        no_overlap = Text(Point(5, 1), "The circles do not overlap")
        no_overlap.draw(win)

    win.getMouse()
    win.close()


def main():
    addTens([5, 2, -3])
    squareEach([3, 5.2, 7])
    sumList([3, 5.2, 7])
    toNumbers(["3", "5.2", "7"])
    writeSumOfSquares()
    starter()
    leapYear(2000)
    circleOverlap()


main()
