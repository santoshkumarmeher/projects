#Password Generator

import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
print("Welcome to password genarator")
in_letters=int(input("How many letters would you like in your password ? \n"))
in_numbers=int(input("How many number would you like in your password ? \n"))
password=''
#easy level
# password=""
# for char in range(1,in_letters+1):
#     password+=random.choice(letters)
# for num in range(1,in_numbers+1):
#     password+=random.choice(numbers)
# print(password)

#hard level

password_list=[]
for char in range(1,in_letters+1):
    password_list+=random.choice(letters)
for num in range(1,in_numbers+1):
    password_list+=random.choice(numbers)
random.shuffle(password_list)
print(password_list)
for char in password_list:
    password+=char
print(password)