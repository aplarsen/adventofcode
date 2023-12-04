import re

sum = 0

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('input.txt') as f:
    for line in f:
        numbers = []

        for i, char in enumerate(line):
            if char in [str(x) for x in range(1, 10)]:
                numbers.append(char)
            else:
                for digit, word in enumerate(digits):
                    if line[i:i+len(word)] == word:
                        numbers.append( str(digit) )

        value = f"{numbers[0]}{numbers[-1]}"

        sum = sum + int(value)

print(sum)