import random

filename = "ip.log.txt"
with open(filename, "w") as file:
    for j in range(10000):
        result = str(random.randint(1, 255))
        for i in range(3):
            result += "." + str(random.randint(0, 255))
        if j != 0:
            file.write("\n" + result)
        else:
            file.write(result)
