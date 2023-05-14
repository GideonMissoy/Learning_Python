# This is a simple program to explore lists, how to display, access and manipulate lists.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1]) #Access a single element using their index
print(bicycles[0].title()) #Manipulating accessed element using methods

message = f"My first bicycle was a {bicycles[2].title()}"
print(message) #Using f-strings to create a message based on an individual value from list
