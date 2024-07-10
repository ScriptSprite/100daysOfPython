# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

bmi = weight / height ** 2

print(int(bmi))

if bmi < 18.5:
  print(f"Your BMI is {bmi:.2f}, you are underweight.")
elif 18.5 <= bmi < 25.0:
  print(f"Your BMI is {bmi:.2f},  have a normal weight.")
elif 25.0 <= bmi < 30.0:
  print(f"Your BMI is {bmi:.2f}, you are slighty overweight.")
elif 30.0 <= bmi < 35.0:
  print(f"Your BMI is {bmi:.2f}, you are obese.")
else:
  print(f"Your BMI is {bmi:.2f},you are clinically obese.")



