# adding all numbers
n=int(input("enter the number range to add all number from 1: "))
total=0
for number in range(1,n+1):
    total += number
print(f"sum of all numbers is {total}")

# adding even number

n=int(input("enter the number of range to add all even number from 1: "))
even_sum=0
for even in range(2,n+1,2):
    even_sum += even
print(f"The sum of all even number is: {even_sum}")

#alternate way

# n = int(input("enter the number of range to add all even number from 1: "))
# even_sum = 0
# for even in range (2,n+1):
#     if even % 2 == 0:
#         even_sum+=even
# print(f"sum of even number is {even_sum}")

# adding odd number

n=int(input("enter the number of range to add all odd number from 1: "))
odd_sum=0
for odd in range(1,n+1,2):
    odd_sum += odd
print(f"The sum of all odd number is: {odd_sum}")

# alternate way for sum of odd number

# n = int(input("enter the number of range to add all odd number from 1: "))
# odd_sum = 0
# for odd in range (1,n+1):
#     if odd % 2 == 1:
#         odd_sum+=odd
# print(f"sum of odd number is {odd_sum}")

