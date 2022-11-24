# In this exercise you will create a Python program that identifies the longest word(s) in a file.
# Your program should output an appropriate message that includes the length of the longest word, along with all of the words of that length
# that occurred in the file. Treat any group of non-white space characters
# as a word, even if it includes numbers or punctuation marks.

import sys
import os


def main():
    textFile = input()

    # check if the file exist
    if os.path.exists(textFile.strip()) is False:
        print("File cannot be found, please check the name")
        return

    with open(textFile) as f:
        lines = f.read().splitlines()

    for thing in sys.argv:
        print(thing, end=' ')

    myList = []
    for i in lines:
        x = i.split()
        myList.append(x)

    # add all lists together
    myList = [item for sublist in myList for item in sublist]

    # make a list that prints all longest words
    words = []

    # append all biggests string to words
    for i in myList:
        if len(i) == len(max(myList, key=len)):
            words.append(i)

    print(words)


if __name__ == '__main__':
    main()
