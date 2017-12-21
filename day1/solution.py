file = open("input.txt", "r")
captcha = file.read()

last_digit = int(captcha[-2])
total = 0

for digit_char in captcha:
    if not digit_char.isdigit():
        break
    digit = int(digit_char)
    if last_digit == digit:
        total += int(last_digit)
    last_digit = digit

print(total)
