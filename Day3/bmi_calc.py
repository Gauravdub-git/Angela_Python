print("BMI CALCULATOR")
weight = float(input("Enter you current weight(in kg) = "))
height = float(input("Enter your Height(in m) = "))

bmi = int(weight) /float(height) **2
bmi_as_int= int(bmi)
print(bmi_as_int)
if bmi_as_int < 18:
    
    print("you are underweight")

elif bmi_as_int == 25:
    print("you have normal weight")

elif bmi_as_int > 25:
    print("You are clinically overweight")

elif bmi_as_int > 30:
    print("you are obese")

else:
    print(bmi_as_int)


