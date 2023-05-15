# This is a simple program to explore lists, how to display, access and manipulate lists.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1]) #Access a single element using their index
print(bicycles[0].title()) #Manipulating accessed element using methods

message = f"My first bicycle was a {bicycles[2].title()}"
print(message) #Using f-strings to create a message based on an individual value from list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
#Adding a new element at the end of the list
motorcycles.append('honda')
print(motorcycles)

#Inserting a new element at any position in the list
motorcycles.insert(0, 'BMW')
print(motorcycles)

# Removing an item from a list
del motorcycles[3]
print(motorcycles)

#Removing an item using the pop() method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki', 'BMW', 'Ducati']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")
first_owned = motorcycles.pop(0)
print(f"The first motorcyle I owned was a {first_owned.title()}")

#Removing an item when you don't know its index
motorcycles = ['honda', 'yamaha', 'suzuki', 'BMW', 'Ducati']
motorcycles.remove('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'BMW', 'Ducati']
too_expensive = 'Ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")