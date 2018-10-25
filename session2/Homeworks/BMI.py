print("BMI calculator.")

m = float(input("Please enter your weight in kg: "))
h = float(input("Please enter your height in cm: "))

h = h/100
bmi = m/h/h

if bmi<16:
    print(" Severely underweight.")
elif bmi<18.5:
    print(" Underweight.")
elif bmi<25:
    print(" Normal.")
elif bmi<30:
    print(" Overweight.")
else:
    print(" Obese.")