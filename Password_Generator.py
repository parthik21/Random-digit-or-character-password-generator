import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?0123456789'

number = input("How many passwords you want to generate? : ")
number = int(number)

length = input("Enter length of passwords : ")
length = int(length)

print("\nHere is your passwords ")
for i in range(number):
    password = ''
    for j in range(length):
        password += random.choice(characters)

    print(password) 