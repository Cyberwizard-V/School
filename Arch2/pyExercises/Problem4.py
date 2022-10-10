"""
In this exercise you will write a function named "is_integer" that determines whether or not the characters in a string represent a valid integer. 
When determining if a string represents an integer you should ignore any leading or trailing white space. Once this white space is ignored, 
a string represents an integer if its length is at least 1 and it only contains digits, or if its first character is either + or - and 
the first character is followed by one or more characters, all of which are digits. Write a main program that reads a string from the user and 
reports whether or not it represents an integer.

Extended version: Extend your program with a different function "remove_non_integer" that if the given input string contains mixed digits and some alphabetic characters, 
it removes the alphabetic characters and prints the remaining integer. 
Example: given -12R0A89s the program will generate -12089. The ersult of +012R0A89s will be 12089
"""
#I'm trying to get better with comments. I hope I'm doing it right.

def is_integer(string):
    #remove white spaces
    string = string.strip()
    #check if the string is empty
    if string == "":
        return(False)
    #check if the string is a digit
    elif string.isdigit():
        return(True)
    #check if the string is a digit with a sign
    elif string[0] == "+" or string[0] == "-":
        if string[1:].isdigit():
            return(True)
        else:
            return(False)
    else:
        return(False)

def remove_non_integer(string):
    #remove white spaces
    string = string.strip()
    #check if the string is empty
    if string == "":
        return("Empty string")
    #check if the string is a digit
    elif string.isdigit():
        return(string)
    #check if the string is a digit with a sign
    elif string[0] == "+" or string[0] == "-":
        if string[1:].isdigit():
            return(string)
        else:
            #remove non digits
            string = string[0] + string[1:].replace(string[1:], "")
            return(string)
    else:
        #remove non digits
        string = string.replace(string, "")
        return(string)

def main():
    #input
    string = input("Enter a string: ")
    #check if the string is an integer
    if is_integer(string) == True:
        print("valid")
    else:
        print("invalid")
    #remove non integer
    print(remove_non_integer(string))


#Tbh i forgot what i was doing here.....
if __name__ == "__main__":
    main()


