import re

file = open("input.txt", "r")

values = [[int(val_string) for val_string in re.split("\W+", line) if val_string.isdigit()] for line in file.readlines()]
differences = [max(val_list) - min(val_list) for val_list in values]

print(sum(differences))
