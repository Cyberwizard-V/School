def check_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b is True:
        return(False)
    else:
        return(True)


def main():
    a = float(input("Enter the first length: "))
    b = float(input("Enter the second length: "))
    c = float(input("Enter the third length: "))
    if check_triangle(a, b, c) is True:
        print("Possible")
    else:
        print("Impossible")


if __name__ == "__main__":
    main()