"""
Name: Lydia Heath
lab7.py
"""


import math


def cash_conversion():
    cash = eval(input("Enter an integer: "))
    print('$' + '{:.2f}'.format(cash))


def encode():
    message = input("Enter message to be encoded: ")
    key = eval(input("Enter key(integer): "))
    acc = ''
    for i in message:
        x = ord(i)
        char = x + key
        new_char = chr(char)
        acc = acc + new_char
    print(acc)


def sphere_area(radius):
    area = 4 * math.pi * (radius**2)
    return area


def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume


def sum_n(n):
    acc = 0
    for i in range(n + 1):
        acc = acc + i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n + 1):
        acc = acc + (i**3)
    return acc


def encode_better():
    message = input("Enter message to be encoded: ")
    key = input("Enter key(word): ")
    acc = ''
    for i in range(len(message)):
        c = ord(message[i])
        k = ord(key[i])
        ch = c + k - 97
        new_ch = chr(ch)
        acc = acc + new_ch
    print(acc)


def main():
    cash_conversion()
    encode()
    print(sphere_area(2))
    print(sphere_volume(5))
    print(sum_n(10))
    print(sum_n_cubes(10))
    encode_better()


main()
