print("Small size = $15")
print("Medium size = $20")
print("Large size = $25")
print("Pepperoni for small pizza is +$2")
print("Pepperoni for medium and large pizza is +3")
print("Extra cheese for any size pizza is +$")

pizza_size=input("Which size of pizza do you want to order 'S','M','L' : ")
pepperoni=input("Do you want Pepperoni: 'Y' or 'N' : ")
extra_cheese=input("Do you want extra cheese ? 'Y' or 'N' : ")
if pizza_size.lower()=="s":
    bill=15
    if pepperoni.lower()=="y":
        bill=bill+2
        if extra_cheese.lower()=="y":
            bill+=1
            print(f"Your bill is ${bill}")
        else:
            print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")
elif pizza_size.lower()=="m":
    bill=20
    if pepperoni.lower()=="y":
        bill=bill+3
        if extra_cheese.lower()=="y":
            bill+=1
            print(f"Your bill is ${bill}")
        else:
            print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")
elif pizza_size.lower()=="l":
    bill=25
    if pepperoni.lower()=="y":
        bill=bill+3
        if extra_cheese.lower()=="y":
            bill+=1
            print(f"Your bill is ${bill}")
        else:
            print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")
else:
    print("Please select valid options")




