import random

def generate_random_password():
    #generate a random length
    length = random.randint(7, 10)
    #generate a random password
    password = ""
    for i in range(length):
        password += chr(random.randint(33, 126))
    return(password)

if __name__ == "__main__":
    print(generate_random_password())