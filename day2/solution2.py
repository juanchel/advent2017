import re

file = open("input.txt", "r")

values = [[int(val_string) for val_string in re.split("\W+", line) if val_string.isdigit()] for line in file.readlines()]
total = 0

for index, val_list in enumerate(values):
    for value_index, value in enumerate(val_list):
        for other in val_list[value_index + 1:]:
            larger = max(value, other)
            smaller = min(value, other)
            if larger % smaller == 0:
                print(larger, smaller)
                total += larger // smaller

print(total)
