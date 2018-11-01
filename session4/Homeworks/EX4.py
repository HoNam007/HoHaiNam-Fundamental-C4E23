answer = [35, 36, 40, 44]
print("Answer the qs:\nif x = 8, the what is the value of 4(x+3)? ")
s = 1 
for i in answer:
    print(s,i, sep='. ')
    s += 1

while True:
    choise = int(input("Your choise: "))
    if choise == 4:
        print("Bingo")
        break
    elif choise in [1, 2, 3]:
        print(":(")
    else:
        print("Four option (1, 2, 3, 4)")
