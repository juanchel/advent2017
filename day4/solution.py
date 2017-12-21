import re

file = open("input.txt", "r")

good = 0

for password in file.readlines():
    words = {}
    ok = True
    for word in re.split('\W+', password):
        if word in words:
            ok = False
            break
        else:
            words[word] = True
    if ok:
        good += 1

print(good)
