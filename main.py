import random
import string
import glob
import os.path

print("-------------------")
print("Password Generator|")
print("-------------------")

pswd = []


def create_file():
    f = open("passwd.txt", "w")
    print("Created file: passwd.txt")
    f.close()
    # f = open("passwd.txt", "a")
    # print("Now the file has more content!!!!!!!!")
    # print()
    # f.write(
    #     "pswd.append(passwords())------ dodany tekst po utworzeniu pliku else: create_file "
    # )
    # f.close()
    # main()


def append_to_file(pswd):
    f = open("passwd.txt", "a")
    print("Now the file has more content!")
    s = "".join(pswd)
    print(pswd)
    f.write(s)
    f.close()
    main()


def gen_passwd(pswd):

    chars = string.ascii_letters + string.digits + string.punctuation
    number = int(input("Amount of password to generate: "))
    length = int(input("Your password length: "))
    print("\n\x1b[5;30;41m" + "Here are your password(s):" + "\x1b[0m")
    pswd = []
    for i in range(number):
        passwords = ""
        for j in range(length):
            passwords += random.choice(chars)
        print(i + 1, "password ->", passwords)
        pswd.append(passwords)
    print(pswd, "lista z dodanymi haslami")

    choice = input("Append to file? yes/no: ")
    match choice:
        case "yes":
            if os.path.isfile("passwd.txt") == True:
                print("OK")
                append_to_file(pswd)
                # f = open("passwd.txt", "a")
                # print("Now the file has more content!")
                # f.write("pswd.append(passwords())")
                # f.close()
                main()
            else:
                print("nie ma ale utowrzse teraz")
                create_file()
                append_to_file(pswd)
        case "no":
            print("Back to main")
            main()


def main():
    choice = input(
        "What would you like to do?\n1.Generate password(s) or q for quit:\n"
    )
    match choice:
        case "1":
            gen_passwd(pswd)
        case "q":
            print("\x1b[5;30;42m" + "QUIT" + "\x1b[0m")
            quit()


main()
