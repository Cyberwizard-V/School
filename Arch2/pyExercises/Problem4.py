def is_integer(string):
    string = string.strip()
    if string == "":
        return(False)
    elif string.isdigit():
        return(True)
    elif string[0] == "+" or string[0] == "-":
        if string[1:].isdigit():
            return(True)
        else:
            return(False)
    else:
        return(False)


def remove_non_integer(x="028jsnd"):
    x = x.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'})
    return x


if __name__ == "__main__":
    checkx = input("Check integer: ")
    if is_integer(checkx):
        print("Valid")
    else:
        print("Invalid")