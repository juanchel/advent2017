import re

file = open("input.txt", "r")

good = 0

for password in file.readlines():
    words = {}
    ok = True
    for word in re.split("\W+", password):
        sorted_word = "".join(sorted(word))
        if sorted_word in words:
            ok = False
            break
        else:
            words[sorted_word] = True
    if ok:
        good += 1

print(good)
