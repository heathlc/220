"""
Name: Lydia Heath
lab3.py
"""


def average():
    num_grades = eval(input("enter number of grades: "))
    acc = 0
    for i in range(num_grades):
        grade = eval(input("enter your grade on HW" + str(i + 1)))
        acc = acc + grade
        avg = acc / num_grades
    print(avg)


def tip_jar():
    acc = 0
    for i in range(5):
        donation = eval(input("enter in amount donated: "))
        acc = acc + donation
    print(acc)


def newton():
    x = eval(input("enter in number: "))
    refine = eval(input("enter how many times to approximate: "))
    approx = x / 2
    for i in range(refine):
        approx = ((approx + (x/approx)) / 2)
    print(approx)


def sequence():
    x = eval(input("enter number of terms: "))
    for i in range(1, x + 1):
        print(1 + (i // 2 * 2))


def pi():
    n = eval(input("enter number of terms: "))
    acc = 1
    for x in range(n):
        numerator = 2 + ((x // 2) * 2)
        denominator = 1 + (((x + 1) // 2) * 2)
        f = numerator / denominator
        acc = acc * f
    print(acc * 2)
