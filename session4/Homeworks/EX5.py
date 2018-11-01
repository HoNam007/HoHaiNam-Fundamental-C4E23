dic = {
    "If x = 8, the what is the value of 4(x+3)? ": [35, 36, 40, 44],
    "1 + 1 =": [1, 2, 3, 4],
    "2 * 2 =": [4, 5, 6, 8],
}
answer = {
    "If x = 8, the what is the value of 4(x+3)? ": 4,
    "1 + 1 =": 2,
    "2 * 2 =": 1,
}
count = 0
for qs in dic:
    print(qs)
    s = 1
    for i in dic[qs]:
        print(s,i, sep='. ')
        s += 1
    while True:
        choise = int(input("Your choise: "))
        if choise == answer[qs]:
            print("Bingo")
            count += 1
            break
        elif choise in [1, 2, 3]:
            print(":(")
            break
        else:
            print("Four option (1, 2, 3, 4)")
print("You correctly answer", count, "out of", len(dic), "questions")