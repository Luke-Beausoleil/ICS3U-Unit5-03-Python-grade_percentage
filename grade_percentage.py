#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# this program receives a level grade and returns a percentage

def percentage(grade):
    if grade == "R":
        mark = 24
    elif grade == "1-":
        mark = 51
    elif grade == "1":
        mark = 54
    elif grade == "1+":
        mark = 58
    elif grade == "2-":
        mark = 61
    elif grade == "2":
        mark = 64
    elif grade == "2+":
        mark = 68
    elif grade == "3-":
        mark = 71
    elif grade == "3":
        mark = 74
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
    print("The middle mark is {0}%\nDone.".format(percentage(grade)))


if __name__ == "__main__":
    main()
