print("\t\t\t Welcome to my BMI calculator\n\n\n")
height = float(input("what is your height in meters : "))
weight = float(input("what is your weight in kg : "))
bmi = weight/(height*height)
print(f"Your BMI is - {bmi:.2f}")

if bmi < 18.5:
    print("Under Weight!")
elif bmi>= 18.5 and bmi<=25:
    print("Normal Weight!")
else:
    print("Overweight!")
