# Using a default value when writing a function.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
# Simplest way to use this function is to provide just a dog's name
describe_pet('harry')
# TO describe an animal other than dog:
describe_pet(animal_type='hamster', pet_name='Otis')