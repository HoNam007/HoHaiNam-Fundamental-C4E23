sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hi, my name is Nam and these are my sheep sizes\n", sizes)

for k in range(4):
    print("MONTH ",k+1)
    for i in range(len(sizes)):
        sizes[i] += 50
    print("One month has passed\n", sizes)  

    maxx = max(sizes)
    print("My biggest sheep has size:", maxx)
    x = sizes.index(maxx)
    sizes[x] = 8
    print("After shearing\n", sizes)
    print()
summ = 0
for j in range(len(sizes)):
    summ += sizes[j]
print("My flock has size in total: ", summ)
print("I would get", summ, "* 2$ =",summ * 2, "$")
