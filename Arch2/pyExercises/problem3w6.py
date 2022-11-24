'''
In an application a valid password must be a combination of digits, uppercase and lowercase letters 
and only four symbols * @ ! ? . 

The length of the password must not be less than 8 characters 
and must not be more than 20 characters. 
In case the password is not valid, the user can try maximum three times until it is validated. 

Implement a Python program that asks the password of the user and checks if it is a valid password.

* Use sets and set operations to solve this problem.
'''

def main():
    password = input("Enter password: ")
    if len(password) < 8 or len(password) > 20:
        print("Invalid password")
        return
    symbols = set("*@!?")
    digits = set("0123456789")
    uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lowercase = set("abcdefghijklmnopqrstuvwxyz")
    password_set = set(password)
    if not symbols.intersection(password_set) or not digits.intersection(password_set) or not uppercase.intersection(password_set) or not lowercase.intersection(password_set):
        print("Invalid password")
        return
    print("Valid password")


if __name__ == "__main__":
    main()