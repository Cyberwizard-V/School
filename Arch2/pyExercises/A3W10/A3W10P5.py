'''
Python uses the # character to mark the beginning of a comment.
The comment ends at the end of the line containing the # character. In this exercise,
you will create a program that removes all of the comments from a Python source file. Check each line in
the file to determine if a # character is present. If it is then your program should remove all of the
characters from the # character to the end of the line (we’ll ignore the situation where the comment character occurs inside of a string).
Save the modified file using a new name that will be entered by the user. T
he user will also enter the name of the input file. Display an appropriate error message if a problem is encountered while accessing the files.
'''


import sys
import os


def main():
    textFile = sys.argv[1]

    # check if the file exist
    if os.path.exists(textFile.strip()) is False:
        print("File cannot be found, please check the name")
        return

    with open(textFile) as f:
        lines = f.read().splitlines()

    for thing in sys.argv:
        print(thing, end='  ')

    z = [x for x in lines if "#" not in x]

    userInput = input("Please enter a filename: ")
    with open(userInput, 'w') as f:
        for line in z:
            f.write(line)
            f.write('\n')


if __name__ == '__main__':
    main()
