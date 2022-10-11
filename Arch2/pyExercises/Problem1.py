import random


def arithmetic_operation(arithmetic_type="summation"):
    if arithmetic_type == "summation":
        summation()
    elif arithmetic_type == "multiplication":
        multiplication()
    elif arithmetic_type == "subtraction":
        subtraction()
    else:
        print("Invalid input")


def summation():
    for i in range(10):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(a, "+", b, "=", end=" ")
        answer = int(input())
        if answer == a + b:
            print("Correct")
        else:
            print("Wrong")


def multiplication():
    for i in range(10):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(a, "*", b, "=", end=" ")
        answer = int(input())
        if answer == a * b:
            print("Correct")
        else:
            print("Wrong")


def subtraction():
    for i in range(10):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(a, "-", b, "=", end=" ")
        answer = int(input())
        if answer == a - b:
            print("Correct")
        else:
            print("Wrong")


if __name__ == "__main__":
    print("What type of arithmetic do you want to practice?")
    print("1. summation")
    print("2. multiplication")
    print("3. subtraction")
    arithmetic_type = input()
    arithmetic_operation(arithmetic_type)