"""
Name: Lydia Heath
weighted_average.py

Problem: Use numeric data from a text file.

Certificate of Authenticity:
I certify this work is entirely my own.
"""


# couldn't get above an 82 on the pytest and am unsure how to fix the math for the failed tests

def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w+')
    in_file = in_file.readlines()
    acc_class = 0
    for line in in_file:
        name = line.split(": ")
        last_first = name[0]
        weight_grades = name[1]
        w_g_split = weight_grades.split(" ")
        w_g_split_list = [int(i) for i in w_g_split]
        w = w_g_split_list[0::2]
        g = w_g_split_list[1::2]
        g[-1] = str(g[-1]).strip()
        w_list = [int(i) for i in w]
        g_list = [int(i) for i in g]
        acc_student = 0
        weighted_grade = [a * b for a, b in zip(g_list, w_list)]
        weights_sum = sum(w_list)
        if weights_sum < 100:
            out_file.write(last_first + "'s average: Error: The weights are less than 100." + "\n")
        elif weights_sum > 100:
            out_file.write(last_first + "'s average: Error: The weights are more than 100." + "\n")
        else:
            for num in weighted_grade:
                acc_student = acc_student + num
            avg = acc_student / 100
            out_file.write(last_first + "'s average: " + str(round(avg, 1)) + "\n")
            acc_class = acc_class + avg
    class_avg = acc_class / len(in_file)
    out_file.write("Class average: " + str(round(class_avg, 1)) + "\n")


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == '__main__':
    main()
