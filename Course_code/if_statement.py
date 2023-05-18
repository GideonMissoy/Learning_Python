# simple if statements
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if-else Statements
age = 17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# The if-elif-else chain.
age = 12
if age < 4:
    print("\nYour admission cost is $0.")
elif age < 18:
    print("\nYour admission cost is $25.")
else:
    print("\nYour admission cost is $40.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}")

#Using multiple elif blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"\nYour admission cost is ${price}")

#Omitting the else block
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"\nYour admission cost is ${price}\n")

# Testing multiple conditions using a series of simple if statements
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")