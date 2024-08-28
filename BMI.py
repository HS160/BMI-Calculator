print("\t\t\t Welcome to my BMI calculator\n\n\n")

height = float(input("what is your height in meters : "))
weight = float(input("what is your weight in kg : "))


bmi = weight/(height*height)

print(f"Your BMI is - {bmi:.2f}")