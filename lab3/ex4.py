from random import randint, choice

op_list = ["+", "-", "*", "/"]
op = choice(op_list)
print(op)
a = randint(0 , 10)
b = randint(0 , 10)
error = randint(-1 , 1)
r1 = a + b + error
r2 = a - b - error
r3 = a * b * error
r4 = a / b / error
if error == "+":
    print(a, "+", b, "=", r1)
elif error == "-":
    print(a, "-", b, "=", r2)
elif error == "*":
    print(a, "*", b, "=", r3)
elif error == "/":
    print(a, "/", b, "=", r4)
else:
    print("Nay")



