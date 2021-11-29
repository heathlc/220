"""
Name: Lydia Heath
lab13.py
"""


from graphics import Rectangle, Point


def is_in_binary(lst, value):
    mid = lst[len(lst) // 2]
    while mid != value and len(lst) != 1:
        if mid > value:
            lst = lst[(mid + 1):]
        else:
            lst = lst[:mid]
        mid = lst[len(lst) // 2]
    if len(lst) == 1 and lst[0] != value:
        return False
    else:
        return True


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i + 1, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy


def rect_sort(rectangles):
    diction = {}
    areas = []
    for rect in rectangles:
        diction[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = diction[areas[i]]


def star_find(filename):
    in_file = open(filename, 'r')
    signals = in_file.read().split()
    found = []
    for i in range(len(signals)):
        pos = i
        if 4000 <= int(signals[i]) <= 5000:
            found.append(signals[i])
        if len(found) == 5:
            break
    print("Five signals have been found.")
    print("The signals are: ", found)
    if len(found) != 5:
        print("Five signals have not been found.")
    else:
        print("The last position was " + str(pos))


def main():
    is_in_binary([1, 2, 3, 4, 5], 2)
    selection_sort([2, 4, 5, 1, 3])
    rect_sort([Rectangle(Point(1, 3), Point(4, 6)), Rectangle(Point(5, 8), Point(9, 14)),
               Rectangle(Point(2, 4), Point(3, 5)), Rectangle(Point(1, 5), Point(6, 11))])
    star_find("signals.txt")


main()
