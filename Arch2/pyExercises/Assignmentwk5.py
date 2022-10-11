import os
import sys

valid_lines = []
corrupt_lines = []
def validate_data(line):

    # split line into list
    line = line.split(",")
    invalid_data = []
    # check if studentnumber is valid
    if len(line[0]) != 7 or line[0][0] != "0" or (line[0][1] != "8" and line[0][1] != "9"):
        corrupt_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + " => INVALID DATA: " + line[0])
    # check if firstname is valid
    elif line[1].isalpha() == False:
        corrupt_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + " => INVALID DATA: " + line[1])
    # check if lastname is valid
    elif line[2].isalpha() == False:
        corrupt_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + " => INVALID DATA: " + line[2])
    # check if date of birth is valid
    elif len(line[3]) != 10 or line[3][4] != "-" or line[3][7] != "-" or line[3][0:4].isdigit() == False or line[3][5:7].isdigit() == False or line[3][8:10].isdigit() == False or int(line[3][0:4]) < 1960 or int(line[3][0:4]) > 2004 or int(line[3][5:7]) < 1 or int(line[3][5:7]) > 12 or int(line[3][8:10]) < 1 or int(line[3][8:10]) > 31:
        corrupt_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + " => INVALID DATA: " + line[3])
    # check if study program is valid
    elif line[4] != "INF" and line[4] != "TINF" and line[4] != "CMD" and line[4] != "AI":
        corrupt_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + " => INVALID DATA: " + line[4])
    # if all checks are passed, add line to valid_lines list
    else:
        valid_lines.append(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4])



def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))
    print('### VALID LINES ###')
    print("\n".join(valid_lines))



if __name__ == "__main__":    
    main('students.csv')