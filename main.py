import random
import string
import os.path

print("-------------------")
print("Password Generator|")
print("-------------------")

pswd = []


def create_file():
    with open("passwd.csv", "w") as file:
        file.close


def append_to_file(pswd):
    with open("passwd.csv", "a") as file:
        for ps in pswd:
            file.write(str(ps) + "\n")
    main()


def gen_passwd(pswd):
    chars = string.ascii_letters + string.digits + string.punctuation
    number = int(input("Amount of password to generate: "))
    length = int(input("Your password length: "))
    print("\n\x1b[5;30;41m" + "Here are your password(s):" + "\x1b[0m")
    for i in range(number):
        passwords = ""
        for j in range(length):
            passwords += random.choice(chars)
        print(i + 1, "password ->", passwords)
        pswd.append(passwords)

    choice = input("Append to file? yes/no: ")
    match choice:
        case "yes":
            if os.path.isfile("passwd.csv") == True:
                append_to_file(pswd)
                main()
            else:
                create_file()
                append_to_file(pswd)
        case "no":
            print("Back to main")
            main()


def main():
    choice = input(
        "What would you like to do?\n1.Generate password(s) or q for quit: \n"
    )
    match choice:
        case "1":
            gen_passwd(pswd)
        case "q":
            print("\x1b[5;30;42m" + "QUIT" + "\x1b[0m")
            quit()


main()
