#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# this program receives a level grade and returns a percentage

def percentage(grade):
    # this function assigns level grades a percentage
    if grade == "R":
        mark = 25
    elif grade == "1-":
        mark = 51
    elif grade == "1":
        mark = 55
    elif grade == "1+":
        mark = 58
    elif grade == "2-":
        mark = 61
    elif grade == "2":
        mark = 65
    elif grade == "2+":
        mark = 68
    elif grade == "3-":
        mark = 71
    elif grade == "3":
        mark = 75
    elif grade == "3+":
        mark = 78
    elif grade == "4-":
        mark = 83
    elif grade == "4":
        mark = 90
    elif grade == "4+":
        mark = 97
    else:
        mark = -1

    return mark


def main():
    # this function receives input and calls another function

    # input
    grade = input("Enter a level grade (i.e. R, 2, 3-, 4+, etc): ")
    # call function
    if percentage(grade) != -1:
        print("The middle mark is {0}%\nDone.".format(percentage(grade)))
    else:
        print("Invalid grade\nDone.")


if __name__ == "__main__":
    main()
