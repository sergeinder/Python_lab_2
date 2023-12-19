def correct_input():
    while True:
        my_mask = input("Enter mask: ")
        list_number = my_mask.split(".")
        try:
            if my_mask.count(".") != 3 and len(list_number) != 4:
                raise ValueError()

            binary_rep = ""
            for element in list_number:
                if 0 > int(element) or int(element) > 255 or list_number[0] == 0:
                    raise ValueError()
                binary_rep += '{0:08b}'.format(int(element))

            if binary_rep.rfind("1") > binary_rep.find("0"):
                raise ValueError()
            return my_mask
        except ValueError:
            print("You input incorrect data, please input correct mask")


mask = correct_input()

bin_mask = ""
for element in mask.split("."):  # Binary representative of mask
    bin_mask += '{0:08b}'.format(int(element))

web_address_list = []
with open("ip.log.txt") as file:  # Reading IP from file
    ip_list = file.read().split("\n")

with open("ip_solve.log.txt", "w") as file:
    writing_number = 0
    for element in ip_list:
        binary_rep = ""
        for el in element.split("."):  # Converting into binary representative
            binary_rep += '{0:08b}'.format(int(el))
        new_binary_rep = binary_rep[0:bin_mask.find("0")] + (len(binary_rep) - bin_mask.find("0")) * "0"

        result = str(int(new_binary_rep[0:8], 2)) + "." \
                 + str(int(new_binary_rep[8:16], 2)) + "." \
                 + str(int(new_binary_rep[16:24], 2)) + "." \
                 + str(int(new_binary_rep[24:], 2))
        if writing_number:
            file.write("\n" + result)
        else:
            file.write(result)
        writing_number += 1
