# How the input() function works
# Following block of code is commented out but runs well
"""message = input("Tell me something, and I will repeat it back to you:\n")
print(message)"""

# Writing clear prompts
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# hAving prompts that spans more than one line. 
# Commenting out following block of code
"""prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your name?"

name = input(prompt)
print(f"\nHello, {name}")
"""

# Using int() to accept numerical input
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print(f"\n{name}, you're tall enough to ride!")
else:
    print(f"Sorry {name}, you'll be able to ride when you're a little older.")
