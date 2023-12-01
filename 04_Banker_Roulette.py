import random
name=input("Enter names seperated by comma")
name_split=name.split(",")
random_name=random.randint(0,(len(name)-1))
print(f"{name} is going to pay the bill ")
