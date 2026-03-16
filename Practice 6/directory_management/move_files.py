import os

source = "test.txt"
destination = "backup/test.txt"

with open(source, 'rb') as file:
    data = file.read()

with open(destination, 'wb') as file:
    file.write(data)

os.remove(source)

print(f"Moved {source} to {destination}")