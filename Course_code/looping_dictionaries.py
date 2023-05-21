# Looping through a dictionary
# Looping through all key-value pairs
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.\n")

# Looping through all the keys in a dictionary
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hello {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values in a dictionary
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(f"\t{language.title()}")

# using a set to pull unique languages in favorite_languages.value()
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(f"\t{language.title()}")