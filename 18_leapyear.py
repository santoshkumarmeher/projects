#Day 3.3

year=int(input("Enter the year to check leap or not: "))
if year%400==0:
    print("This is leaf year")
elif year%100==0:
    print("This is not a leaf year")
elif year%4==0:
    print("year is leaf year")
else:
    print("year is not a leaf year")