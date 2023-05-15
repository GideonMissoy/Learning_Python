# Sorts items in a list permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#Temporarily sorting a link, alphabetically and reversed
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars_Alsorted = sorted(cars)
print(cars_Alsorted)
cars_Revsorted = sorted(cars, reverse=True)
print(cars_Revsorted)

#Printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

#finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))