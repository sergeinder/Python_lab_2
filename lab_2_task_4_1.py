import os
import random

# Creating directory
try:
    os.mkdir("example")
except FileExistsError:
    print("This directory already exist")

# Creating 100 files
for i in range(1, 100 + 1):
    with open("example/file_" + str(i), 'wb') as file:
        file.write(os.urandom(random.randint(1, 100) * 1024))  # urandom - function with size in byte as argument
