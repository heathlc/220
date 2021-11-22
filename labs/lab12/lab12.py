"""
Name: Lydia Heath
lab12.py
"""


from random import randint


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Lydia"
    except:
        pass


def read_data(file_name):
    f = open(file_name, 'r')
    data = f.read()
    data = data.split()
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == i:
            return True
        i = i + 1
    return False


def good_input():
    x = eval(input("enter a number: "))
    while not(1 <= x <= 10):
        x = eval(input("enter a different number: "))
    return x


def num_digits():
    num = eval(input("enter a number: "))
    while num >= 1:
        digits = 0
        while num != 0:
            num = num // 10
            digits = digits + 1
        print("Your number had " + str(digits) + " digits.")
        num = eval(input("enter a number: "))


def hi_lo_game():
    rand_num = randint(1, 100)
    guess = 1
    guess_num = eval(input("guess the number: "))
    while guess_num != rand_num and guess != 7:
        guess = guess + 1
        if guess_num < rand_num:
            print("Your number was too low")
        else:
            print("Your number was too high")
        guess_num = eval(input("guess the number: "))
    if guess_num == rand_num:
        print("You won in " + str(guess) + " guesses!")
    else:
        print("Sorry you lose. The number was " + str(rand_num))


def main():
    read_data("data.txt")
    is_in_linear(7, [1, 4, 5, 7, 8, 9, 10, 2, 3])
    good_input()
    num_digits()
    hi_lo_game()


main()
