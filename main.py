import random
import string

print("Password Generator")


def __init__(self):
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
    # chars = string.ascii_letters + string.digits + string.punctuation
    # number = int(input("Amount of password to generate: "))
    # length = int(input("Your password length: "))
    print("\n\x1b[5;30;41m" + "Here are your password(s):" + "\x1b[0m")

    for i in range(number):
        passwords = ""
        for j in range(length):
            passwords += random.choice(chars)
            print(i, "passwd", passwords)


def main(self):
    choice = input(
        "What would you like to do?\n1.Create file to pass,\n2.Append pass to file, \n3.Gen passwd or q for quit: "
    )
    match choice:
        case "1":
            create_file()
        case "2":
            append_to_file()
        case "3":
            gen_passwd()
        case "q":
            breakpoint
            print("\x1b[5;30;42m" + "QUIT" + "\x1b[0m")


main(main)
