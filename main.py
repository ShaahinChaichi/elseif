# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

BMI = weight / (height ** 2)

print(f"\n{weight} + ({height} x {height}) = {BMI} ")

rnd_BMI = round(BMI)

if BMI < 18.5:
    print(f"Your BMI is {rnd_BMI}, You are underweight")
elif BMI < 25:
    print(f"Your BMI is {rnd_BMI}, You are normal weight")
elif BMI < 30:
    print(f"Your BMI is {rnd_BMI}, You are slighty overweight")
elif BMI < 35:
    print(f"Your BMI is {rnd_BMI}, You are obese")
else:
    print(f"Your BMI is {rnd_BMI}, You are clinically obese")
