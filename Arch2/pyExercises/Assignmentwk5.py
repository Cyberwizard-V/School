"""
A dataset is given with information of students: student number, first name, last name, date of birth, study program. 
You are asked to implement a program that given this dataset (as a csv file), the program processes the information. The requested criteria are:
Sometimes data values are corrupted. The program must report corupted values. Any invalid or empty value is defined as corrupted.

- Student number has this format: 7 digits, starting with 0 and second digit (from left) can be either 9 or 8. Example: 0212345 is not valid
- First name and last names, contains only alphabet.
- Date of birth has this format: YYYY-MM-DD. Days between 1 and 31, months between 1 and 12 and Years between 1960 and 2004.
- Study program can have one of these values: INF, TINF, CMD, AI.

A template Python file is provided with a function that loads the data set.

The program should make two separate lists: list of rows with correct values and a list of rows with corrupted values. 
These two lists will be printed with this format:
"""
import os
import sys

valid_lines = []
corrupt_lines = []

'''
The validate_data function will check the students.csv line by line for corrupt data.

- Valid lines should be added to the valid_lines list.
- Invalid lines should be added to the corrupt_lines list.

Example input: 0896801,Kari,Wilmore,1970-06-18,INF
This data is valid and the line should be added to the valid_lines list unchanged.

Example input: 0773226,Junette,Gur_ry,1995-12-05,
This data is invalid and the line should be added to the corrupt_lines list in the following format:

0773226,Junette,Gur_ry,1995-12-05, => INVALID DATA: ['0773226', 'Gur_ry', '']

In the above example the studentnumber does not start with '08' or '09', 
the last name contains a special character and the student program is empty.

Don't forget to put the students.csv file in the same location as this file!
''' 
def validate_data(line):

    # split line into list
    line = line.split(",")
    # check if studentnumber is valid
    if len(line[0]) != 7 or line[0][0] != "0" or (line[0][1] != "8" and line[0][1] != "9"):
        corrupt_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + " => INVALID DATA: " + str(line))
    # check if firstname is valid
    elif line[1].isalpha() == False:
        corrupt_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + " => INVALID DATA: " + str(line))
    # check if lastname is valid
    elif line[2].isalpha() == False:
        corrupt_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + " => INVALID DATA: " + str(line))
    # check if date of birth is valid
    elif len(line[3]) != 10 or line[3][4] != "-" or line[3][7] != "-" or line[3][0:4].isdigit() == False or line[3][5:7].isdigit() == False or line[3][8:10].isdigit() == False or int(line[3][0:4]) < 1960 or int(line[3][0:4]) > 2004 or int(line[3][5:7]) < 1 or int(line[3][5:7]) > 12 or int(line[3][8:10]) < 1 or int(line[3][8:10]) > 31:
        corrupt_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + " => INVALID DATA: " + str(line))
    # check if study program is valid
    elif line[4] != "INF" and line[4] != "TINF" and line[4] != "CMD" and line[4] != "AI":
        corrupt_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + " => INVALID DATA: " + str(line))
    # if all checks are passed, add line to valid_lines list
    else:
        valid_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4])



def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":    
    main('students.csv')