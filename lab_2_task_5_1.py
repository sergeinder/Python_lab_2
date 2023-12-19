import os


def correct_input():
    while True:
        try:
            number = int(input("Enter your positive number < 100: "))
            if number < 1 or number > 100:
                raise ValueError
            return number

        except ValueError:
            print("You entered incorrect data")


left = correct_input()
right = correct_input()

file_counter = 0
for number_of_file in range(1, 100 + 1):
    size = os.path.getsize("example/file_" + str(number_of_file))
    if left <= size // 1024 <= right:
        file_counter += 1

print("Nuber of file with correct size: ", file_counter)
