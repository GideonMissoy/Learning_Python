# Using keyword arguments in a function call
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
"""Keyword arguments, unlike positional arguments, doesn't return unexpected results
when you mix up the order of the arguments in a function call."""