# This is to introduce and explore the range function.
# The fxn below prints 1 through 4
for value in range(1, 5):
    print(value)

# The function below prints 1 through 5
for value in range(1, 6):
    print(value)

#Using range to print a list of numbers
numbers = list(range(1, 6))
print(numbers)

#Using range fxn to tell python to skip numbers in a given range
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#Using the range function to print a list of the first 10 squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)