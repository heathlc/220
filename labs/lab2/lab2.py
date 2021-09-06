"""
Name: Lydia Heath
lab2.py
"""


import math


def sum_of_threes():
    upper_bound = eval(input("Enter upper bound: "))
    acc = 0
    for x in range(0, upper_bound + 1, 3):
        acc = acc + x
    print(acc)


sum_of_threes()


def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(l * h, end=" ")
        print()


multiplication_table()


def triangle_area():
    side_a = eval(input("Enter length of side a: "))
    side_b = eval(input("Enter length of side b: "))
    side_c = eval(input("Enter length of side c: "))
    s = (side_a + side_b + side_c) / 2
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    print(area)


triangle_area()


def sum_squares():
    lower_range = eval(input("Enter lower range value: "))
    upper_range = eval(input("Enter upper range value: "))
    acc = 0
    for x in range(lower_range, upper_range + 1):
        acc = acc + (x**2)
    print(acc)


sum_squares()


def power():
    base = eval(input("Enter base value: "))
    exponent = eval(input("Enter exponent value: "))
    acc = 1
    for x in range(exponent):
        acc = acc * base
    print(base, "^", exponent, "=", acc)


power()
