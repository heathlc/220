"""
Name: Lydia Heath
hangman.py
"""

from random import randint


def words(file):
    in_file = open(file, "r")
    contents = in_file.read()
    list_of_words = contents.split("\n")
    return list_of_words


def random_word(list_word):
    return list_word[randint(0, len(list_word) - 1)]


def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)


def won(word, letters):
    x = fill(word, letters)
    if x == word:
        answer = True
    else:
        answer = False
    return answer


def hangman():
    w = words("wordlist.txt")
    secret_word = random_word(w)
    incorrect = 0
    guesses = []
    current = "_" * len(secret_word)
    while not won(secret_word, guesses) and incorrect < 7:
        display = fill(secret_word, guesses)
        print(display)
        print("guesses: ", guesses)
        letter = input("enter a letter: ")
        while letter in guesses:
            letter = input("enter another letter:")
        guesses.append(letter)
        display = fill(secret_word, guesses)
        if letter not in secret_word:
            incorrect = incorrect + 1
        else:
            current = display
    if incorrect == 7:
        print("You lost.")
    else:
        print(current)
        print("You won!")


def main():
    hangman()


main()
