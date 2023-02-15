import random
import string

print("Password Generator")


def create_file():
    f = open("passwd.txt", "w")
    print("Created file: passwd.txt")
    f.close()
    main()


def append_to_file():
    f = open("passwd.txt", "a")
    print("Now the file has more content!")
    f.write("asdsadas")
    f.close()
    main()


def gen_passwd():
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
    print(pswd)

    choice = input("Append to file? y/n")
    match choice:
        case "y":
            f = open("passwd.txt", "a")
            print("Now the file has more content!")
            f.write("pswd.append(passwords())")
            f.close()
        case "n":
            main()


def main():
    choice = input(
        "What would you like to do?\n1.Create file to pass,\n2.Gen passwd or q for quit: "
    )
    match choice:
        case "1":
            create_file()
        case "2":
            gen_passwd()
        case "q":
            print("\x1b[5;30;42m" + "QUIT" + "\x1b[0m")
            quit()


main()
