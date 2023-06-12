from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
             'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

"""
Assuming only siddhartha.txt file is not found:
Using the try-except block provides 2 significant advantages:
1. We prevent our users from seeing a traceback
2. We let the program continue analyzing the tests it's able to find.
If we don't catch the FileNotFoundError that siddhartha.txt raises,
the user would see a full traceback, and the program would stop running after
trying to analuze Siddhartha. It would never analyze Moby Dick and Little Women.
"""