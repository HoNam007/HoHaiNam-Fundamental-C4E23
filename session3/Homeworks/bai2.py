print("Hi there, this is a superuser hateway")

username = input("Username: ")

while True:
    if username != "c4e":
        print("You are not superuser")
        username = input("Username: ")

    else:
        password = input("Password: ")
        if password != "codethechange":
            print("Password is incorrect")
        else:
            print("Welcome, c4e")
            break