'''
Implement a program that determines and displays the number of unique characters in a string 
entered by the user. For example, Hello, World! has 10 unique characters while zzz has only 
one unique character.

* Use only dictionaries to solve this problem (create a function: unique_chars_dict).
* Use only sets to solve this problem (create a function: unique_chars_set).
* Which solution would you prefer?
'''
char_dict = dict()

def unique_chars_set(string):
    return len(set(string))


def unique_chars_dict(string):
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    unique_chars = 0
    for char in char_dict:
        unique_chars += 1

    return unique_chars


def main():
    string = input("Enter a string: ")
    print("Number of unique characters (dictionary):", unique_chars_dict(string))

if __name__ == "__main__":
    main()

