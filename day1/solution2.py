file = open("input.txt", "r")
captcha = file.read()

total = 0
jump = (len(captcha) - 1) // 2

for index, digit_char in enumerate(captcha[0:jump]):
    if not digit_char.isdigit():
        break
    digit = int(digit_char)
    other_digit_char = captcha[index + jump]
    other_digit = int(other_digit_char)
    if digit == other_digit:
        total += 2 * digit

print(total)
