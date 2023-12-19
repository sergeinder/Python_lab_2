import csv

# Reading .csv file
with open("players.csv", "r", newline='', encoding="utf8") as file:
    reader = csv.reader(file)
    my_dict = {}
    i = 0
    for element in reader:
        if i:
            my_dict[element[0]] = [int(element[1]), int(element[2])]
        i += 1

result = [["Sportsman", "position"]]
mx_wins = sorted(set([my_dict[key][0] for key in my_dict]), reverse=True)

position = 1
for element in mx_wins:
    new_dict = {}
    for key in my_dict:  # For watching how many players have this number of wins
        if my_dict[key][0] == element:
            new_dict[key] = my_dict[key]

    # Compare additional score
    add_point = []
    for key in new_dict:
        add_point.append(new_dict[key][-1])

    for el in sorted(set(add_point), reverse=True):
        for key in new_dict:
            if new_dict[key][-1] == el:
                result.append([key, position])
        position = len(result)

# Writing result in .csv file
with open("results.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(result)
