"""
Name: Lydia Heath
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total = eval(input("Enter total shots: "))
    made = eval(input("Enter shots made: "))
    percentage = (made / total) * 100
    print("Shooting Percentage =", percentage, "%")


def coffee():
    pounds = eval(input("Number of pounds ordered: "))
    beans = 10.50
    shipping = 0.86
    order = 1.50
    total = (pounds * beans) + (pounds * shipping) + order
    print("Total Cost = $", total)


def kilometers_to_miles():
    kilometers = eval(input("Enter kilometers: "))
    miles = kilometers / 1.61
    print("Miles =", miles)
