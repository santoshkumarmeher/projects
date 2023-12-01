#Day 3.2
print("""BMI index 
      BMI<=18.5 (Under weight) 
      18.5>= BMI <25 (Normal Weight)
      25>= BMI <30 (Over Weight)
      30>= BMI <35 (Obese)
      BMI>= 35 (Clinically Obese)
      """)
weight=int(input("Enter your weight in kg: "))
height_in_cm=int(input("Enter your height in cm: "))
height=height_in_cm/100
BMI=round(weight/height**2)
if BMI<18.5:
    print(f" your BMI is {BMI} you are under weight")
elif BMI<=25:
    print(f"your BMI is {BMI} You are normal weight")
elif BMI<=30:
    print(f" your BMI is {BMI} your are Over weight")
elif BMI<=35:
    print(f"your BMI is {BMI} You are Obese")
else:
    print(f"your BMI is {BMI} your are Clinically Obese")