"""
Name: Lydia Heath
mean.py

Problem: Calculating different means.

Certificate of Authenticity:
I certify this project is entirely my own work.
"""


# the program will calculate the RMS average, harmonic mean, and geometric mean
# the inputs will be the amount of numbers to be averaged and the value of the numbers
# the outputs will be the average values of each type of mean being solved for in the program
# the program must first prompt the user for the amount of values that will be averages
# second, it will ask the user for the values of the numbers to be averaged
# the program will then calculate the RMS average, then the harmonic mean, and the geometric mean
# last it will print each of the average values


import math


def main():
    average_amount = eval(input("enter number of values to be averaged: "))
    acc = 0
    har_acc = 0
    geo_acc = 1
    for i in range(average_amount):
        values = eval(input("enter in numerical value of number: "))
        acc = acc + (values**2)
        avg = acc / average_amount
        rms = math.sqrt(avg)
        har_acc = har_acc + (1/values)
        har_mean = average_amount / har_acc
        geo_acc = geo_acc * values
        geo_mean = geo_acc**(1/average_amount)
    print(round(rms, 3))
    print(round(har_mean, 3))
    print(round(geo_mean, 3))


if __name__ == '__main__':
    main()
