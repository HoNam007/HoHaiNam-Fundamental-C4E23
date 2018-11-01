items = ['T-Shirt', 'Sweater']

hi = input("Welcome to our shop, what do you want (C, R, U, D)? ")

while True:
    if hi == "r" or hi == "R":
        print("Our items: ", end='')
        print(*items, sep=', ')
        hi = input("Welcome to our shop, what do you want (C, R, U, D)? ")

    elif hi == "c" or hi == "C":
        new_item =  input("Enter new item: ")
        items.append(new_item)
        print("Our items: ", end='')
        print(*items, sep=', ')
        hi = input("Welcome to our shop, what do you want (C, R, U, D)? ")

    elif hi == "u" or hi == "U":
        update = input("Update position? ")
        while not update.isdigit():
            print("Please enter the number")
            update = input("Update position? ")

        update = int(update)
        while update > len(items):
            update = input("Update position? ")

        new_item2 = input("New item? ")
        items[update - 1] = (new_item2)
        print("Our items: ", end='')
        print(*items, sep=', ')
        hi = input("Welcome to our shop, what do you want (C, R, U, D)? ")

    elif hi == "d" or hi == "D":
        dele = input("Delete position? ")
        while not dele.isdigit():
            print("Please enter the number")
            dele = input("Update position? ")
        dele = int(dele)
        while dele > len(items):
            dele = input("Update position? ")
        items.pop(dele - 1)
        print("Our items: ", end='')
        print(*items, sep=', ')
        hi = input("Welcome to our shop, what do you want (C, R, U, D)? ")

    else:
        hi = input("Welcome to our shop, what do you want (C, R, U, D)? ")
