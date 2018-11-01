sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hi, my name is Nam and these are my sheep sizes\n", sizes)

maxx = max(sizes)
print("My biggest sheep has size:", maxx)
x = sizes.index(maxx)
sizes[x] = 8

print("After shearing\n", sizes)

for i in range(len(sizes)):
    sizes[i] += 50
print("One month has passed\n", sizes)  
