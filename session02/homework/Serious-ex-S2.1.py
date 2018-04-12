h=(float(input("Your height (cm): ")))
h1=h/100
w=(float(input("Your weight (kg): ")))
b=w/(h1**2)
print("BMI", b)
if b<16:
    print("Severely underweight")
elif 16<=b<18.5:
    print("Underweight")
elif 18.5<=b<25:
    print("Normal")
elif 25<=b<30:
    print("Overweight")
else:
    print("Obese")
