"""
Name: Lydia Heath
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter name (First Last): ")
    name_list = name.split(' ')
    print(name_list[-1], ',', name_list[0])


def company_name():
    domain = input("Enter web domain: ")
    domain_list = domain.split('.')
    print(domain_list[1])


def initials():
    num_students = eval(input("Enter number of students: "))
    for i in range(num_students):
        first = input("Enter the first name of student " + str(i + 1) + ":")
        last = input("Enter " + first + "'s last name:")
        print(first + "'s initials are: " + first[0] + last[0])


def names():
    name = input("Enter names (first and last), separated by commas: ")
    name = name.split(", ")
    for i in name:
        name_list = i.split(" ")
        first = name_list[0][0]
        last = name_list[1][0]
        print(first + last, end=" ")


def thirds():
    num_sentences = eval(input("Enter number of sentences: "))
    for i in range(num_sentences):
        sentences = input("Enter sentence " + str(i + 1) + ":")
        print(sentences[2::3])


def word_average():
    num_sentence = eval(input("Enter number of sentences: "))
    for i in range(num_sentence):
        sentence = input("Enter sentence " + str(i + 1) + ":")
        sentence = sentence.split(" ")
        acc = 0
        for word in sentence:
            acc = acc + len(word)
        avg = acc / len(sentence)
        print(avg)


def pig_latin():
    sentence = input("Enter sentence: ")
    sentence = sentence.lower()
    sentence = sentence.split(" ")
    for word in sentence:
        x = word[1:]
        x = x + word[0] + "ay"
        print(x, end=" ")


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()


main()
