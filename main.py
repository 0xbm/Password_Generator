import random
import string

print("Password Generator")

chars = string.ascii_letters + string.digits + string.punctuation

number = int(input("Amount of password to generate: "))
length = int(input("Your password length: "))


def create_file():
    f = open("passwd.txt", "w")
    f.write("Created new file")
    f.close()


def append_to_file():
    f = open("passwd.txt", "a")
    f.write("Now the file has more content!")
    f.close()


def gen_passwd():
    print("\n\x1b[5;30;41m" + "Here are your password(s):" + "\x1b[0m")

    for i in range(number):
        passwords = ""
        for c in range(length):
            passwords += random.choice(chars)
            print(i, "passwd", passwords)
