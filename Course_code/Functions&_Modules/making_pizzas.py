import pizza #This line tells python to open the file pizza.py,
# and copy all the functions from it into this program

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Importing a specific module.
from pizza import make_pizza # With this syntax, you don't need to use the dot notation
# when you call a function. Because we've explicitly imported the function make_pizza()
# in the import statement, we can call it by name when we use the function.

make_pizza(16, 'pepperoni')