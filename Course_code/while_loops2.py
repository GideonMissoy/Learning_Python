""" Using a while loop with lists and dictionaries. 
1. Moving items from one list to another"""

# Start with users that need to be verified,
# and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unverified users.
# move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(f"\t{confirmed_user.title()}")

# 2. Removing all instances of specific values from a list.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# 3. Using a while loop to fill a dictionary with user input.
responses = {}
#set a flag to indicate that polling is active
polling_active = True

while polling_active:
    #prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb? ")
    
    #Store the response in the dictionary
    responses[name] = response
    
    #find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#polling is complete. show the results.
print(f"\n{responses}")
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")