################################################

# print("Welcoe to roller coster: ")
# height=int(input("Enter your height in cm: "))
# if height>120:
#     print("your can the ride roller coster ")
# else:
#     print("You are not eligible for rollercoster")

################################################

# print("Welcoe to roller coster ")
# height=int(input("Enter your height in cm: "))
# if height>120:
#     print("your can the ride roller coster ")
#     age=int(input("What is your age: "))
#     if age>=18:
#         print(("Please buy $12 ticket"))
#     else:
#         print("please buy $7 ticket")
# else:
#     print("You are not eligible for rollercoster")

###########################################################

# print("Welcoe to roller coster ")
# height=int(input("Enter your height in cm: "))
# if height>120:
#     print("your can the ride roller coster ")
#     age=int(input("What is your age: "))
#     if age>18:
#         print(("Please buy $12 ticket"))
#     elif age<=12:
#         print("please buy $5 ticket")
#     else:
#         print("Please buy $7 ticket")
# else:
#     print("You are not eligible for rollercoster")

###################################################

print("Welcoe to roller coster ")
height=int(input("Enter your height in cm: "))
if height>120:
    print("your can the ride roller coster ")
    age=int(input("What is your age: "))
    if age<12:
        bill=5
        print(("Please buy $5 ticket"))
    elif age<18:
        bill=7
        print("please buy $7 ticket")
    elif age>45 and age<55:
        bill=0
        print("You are eligible for free ticket")
    else:
        bill=12
        print("Please buy $12 ticket")
    photo=input("If you want photo choose 'Y'")
    if photo.lower()=="y":
        bill+=3
    print(f"your final bill is {bill}" )

else:
    print("You are not eligible for rollercoster")

