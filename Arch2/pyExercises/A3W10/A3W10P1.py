# Unix-based operating systems usually include a tool named head. It displays the first 10 lines of a file 
# whose name is provided as a command line parameter. Write a Python program that provides the same behavior. Display an appropriate 
# error message if the file requested by the user does not exist or if the command line parameter is omitted.
import sys
import os

def main():
    textFile = sys.argv[1]

     # check if the file exist
    if os.path.exists(textFile.strip()) is False:
        print("File cannot be found, please check the name")
        return


    with open(textFile) as f:
        lines = f.readlines()

    for thing in sys.argv:
        print(thing, end='  ')

    #get last 10
    #lastLines = lines[::-10]

    for i in range(10):
        print(f"{lines[i]}", end="")


if __name__ == '__main__':
    main()