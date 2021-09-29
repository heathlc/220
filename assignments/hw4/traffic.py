"""
Name: Lydia Heath
traffic.py

Problem: Accumulating road surveys.

Certificate of Authenticity:
I certify this project is entirely my own work.
"""


def main():
    roads = eval(input("Enter how many roads were surveyed: "))
    tot = 0
    for i in range(roads):
        acc = 0
        days = eval(input("How many days was road " + str(i + 1) + " surveyed: "))
        for _ in range(days):
            cars = eval(input("How many cars traveled on day " + str(_ + 1) + ":"))
            acc = acc + cars
        avg = acc / days
        print("Road", str(i + 1), "average vehicles per day:", round(avg, 2))
        tot = tot + acc
    avg_per_road = tot / roads
    print("Total number of vehicles traveled on all roads: ", tot)
    print("Average number of vehicles per road:", round(avg_per_road, 2))


if __name__ == '__main__':
    main()
