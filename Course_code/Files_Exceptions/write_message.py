from pathlib import Path

contents = "I love programming.\n"
contents += "I love writing code for new games.\n"
contents += "I laso love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)