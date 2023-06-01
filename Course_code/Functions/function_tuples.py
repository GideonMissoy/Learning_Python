# Passing an arbitrary number of arguments to a function.
# Returns a tuple
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Replacing the print() call with a loop that runs through the list of toppings
# and describes the pizza being ordered.
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping.title()}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')