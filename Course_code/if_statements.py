# Illustrating a simple implementation of an if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#checking for equality
car = 'bmw'
if car == 'bmw':
    print("True")
else:
    print("False")

#Checking for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("\nHold the anchovies!")

# Numerical comparison
age = 18
if age == 18:
    print("True")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# Using mathematical comparisons
age = 19
if age >= 21:
    print("Drink responsibly")
else:
    print("Drinking is restricted to persons under age of 21")

# Sample of using 'and' to check multiple conditions
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print(True)
else:
    print("Both conditions haven't been met")
