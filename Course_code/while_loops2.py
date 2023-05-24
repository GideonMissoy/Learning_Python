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