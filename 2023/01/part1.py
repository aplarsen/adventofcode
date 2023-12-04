import re

sum = 0

with open('input.txt') as f:
    for line in f:
        numbers = re.sub( r'[^\d]', '', line )

        value = f"{numbers[0]}{numbers[-1]}"

        sum = sum + int(value)

print(sum)