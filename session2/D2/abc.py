a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

delta = b*b - 4*a*c

if delta < 0:
    print("No solution")
elif delta == 0: # !=
    x = -b / (2 * a)
    print("1 solution")
else:
    delta_sprt = delta**0.5
    x1 = (-b + delta_sprt) / a_2
    x2 = (-b + delta_sprt) / a_2
    print("2 solution", x1 , x2)
