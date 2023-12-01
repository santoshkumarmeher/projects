name1=input("Enter your name: ")
name2=input("Enter your partner's name : ")
combine_name=name1+name2
lower_case=combine_name.lower()
t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
true=t+r+u+e
love=l+o+v+e
str_score=str(true)+str(love)
score=int(str_score)
print(f"your love score is {score}")
if score<10 or score>90:
    print("You go together like coke and mentos")
elif score>40 and score<50:
    print("you are alright together")



