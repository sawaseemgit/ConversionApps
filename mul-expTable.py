import math as m

print("Welcome to Multiplication/Exponential Table Program")

name = input("Hello, what is your Name? ").title().strip()
number = float(input("What number would you like to work with? "))
print(f'Multiplication Table for {number} is: ')
for i in range(1, 10):
    print(f'\t{i}  *  {number} = {round((i * number), 4)}')

print(f'Exponential Table for {number} is:')
for i in range(1, 10):
    print(f'\t{number} ** {i} = {round((m.e ** number), 4)}')
message = name + ", Math is cool"
print(message)
print(f"\t{message.lower()}")
print(f"\t\t{message.upper()}")
print(f"\t\t\t{message.title()}")
