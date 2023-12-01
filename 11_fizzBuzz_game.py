#number divisible by 3 print "fizz"
#number divisible by 5 print "buzz"
#number divisible by 3 & 5 print "fizzbuzz"

number=int(input("Enter the number range for fizzbuzz game "))
for i in range(1,number+1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)