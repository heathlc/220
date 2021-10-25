"""
Name: Lydia Heath
lab8.py
"""


from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w+')
    i = 1
    for line in in_file:
        words = line.split()
        for word in words:
            out_file.write(str(i) + " " + word + "\n")
            i = i + 1
    in_file.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    for line in in_file:
        parts = line.split()
        wage = float(parts[2])
        wage_add = 1.65
        wages = wage + wage_add
        out_file.write(str(parts[0]) + " " + str(parts[1]) + " " +
                       str(wages) + " " + str(wages * float(parts[3])) + "\n")
    in_file.close()
    out_file.close()


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc = acc + int(isbn[i]) * pos
    return acc


def send_message(file, friend):
    in_file = open(file, 'r')
    out_file = open(friend + ".txt", 'w')
    for line in in_file:
        out_file.write(line)
    in_file.close()
    out_file.close()


def send_safe_message(file, friend, key):
    in_file = open(file, 'r')
    out_file = open(friend + ".txt", 'w')
    for line in in_file:
        out_file.write(encode(line, key))
    in_file.close()
    out_file.close()


def send_uncrackable_message(file, friend, pad):
    pad_file = open(pad, 'r')
    key = pad_file.read()
    in_file = open(file, 'r')
    out_file = open(friend + ".txt", 'w')
    for line in in_file:
        out_file.write(encode_better(line, key))
    in_file.close()
    out_file.close()


def main():
    number_words("Walrus.txt", "W_out.txt")
    hourly_wages("hourly_wages.txt", "hourly_wages_out.txt")
    calc_check_sum("0072946520")
    send_message("message.txt", "alice")
    send_safe_message("secret_message.txt", "bob", 5)
    send_uncrackable_message("safest_message.txt", "charlie", "pad.txt")


main()
