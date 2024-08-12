print("Check your BMI(Body Mass Index) and find out if you're underweight, overweight, or in a healthy range for your height and age with this BMI calculator.")

weight = float(input("What is your weight in kg?"))
height = float(input("What is your height in meter?"))

bmi = weight / (height*height)
round_bmi = round(bmi, 1)

print("Your BMI is", round_bmi)

if bmi < 18.5: 
    print("A BMI lower than 18.5 means you are underweight.")
elif bmi < 24.9:
    print("You have a healthy weight.") 
elif bmi < 29.9:
    print("You have overweight.")
elif bmi < 35: 
    print("Yoy clinically obese.")
else: 
    print("You are clinically obese.")

