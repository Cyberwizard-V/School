import os
import sys

valid_lines = []
corrupt_lines = []


def validate_data(line):
    dataCSV = line.split(",")
    invalid = []
    studentNumber = dataCSV[0]
    firstName = dataCSV[1]
    lastName = dataCSV[2]
    dateOfBirth = dataCSV[3]
    studyProgram = dataCSV[4]
    y = int(dateOfBirth[:4])
    m = int(dateOfBirth[5:7])
    d = int(dateOfBirth[8:])

    if len(studentNumber) < 7 or studentNumber[0] != "0" or studentNumber[1] not in [
        "8",
            "9"]:
        invalid.append(studentNumber)
    else:
        pass

    if firstName.isalpha():
        pass
    else:
        invalid.append(firstName)

    if lastName.isalpha():
        pass
    else:
        invalid.append(lastName)

    if not 1960 <= y <= 2004 or not 1 <= m <= 12 or not 1 <= d <= 31:
        invalid.append(dateOfBirth)
    else:
        pass

    if studyProgram not in ("INF", "TINF", "CMD", "AI"):
        invalid.append(studyProgram)
    else:
        pass

    if bool(invalid) is False:
        valid_lines.append(line)
    else:
        corrupt_lines.append(f"{line} => INVALID DATA: {invalid}")


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
