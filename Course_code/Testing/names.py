from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease enter your first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    middle = input("Enter a middle name: ")
    if middle == 'q':
        break
    
    formatted_name = get_formatted_name(first, last,)
    print(f"\tNeatly formatted name: {formatted_name}.")