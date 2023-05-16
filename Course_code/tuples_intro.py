# Introducing tuples.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# To define a tuple with one element, include a trailing comma
my_t = (3,)
print(my_t)

# Writing over a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


# A buffer-style restaurant offers only five basic foods.
# Think of five simple foods, and store them in a tuple
foods = ('chapati', 'rice', 'ugali', 'beef stew', 'chicken stew')
print("\nThese are the foods available in our restaurant:")
for food in foods:
    print(food.title())
#The restaurant changes its menu, changing two of the items with different foods
# Add a line that rewrites the tuple then use a for loop to print
foods = ('chapati', 'rice', 'pasta', 'beef stew', 'chicken curry')
print("\nThese are the foods available in our revised menu:")
for food in foods:
    print(food.title())