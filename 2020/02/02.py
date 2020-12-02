import re

# Read lines from input
with open("input.txt") as f:
	lines = f.read().split("\n")

# Initialize a counter for passwords that pass the test
count = 0

# Iterate over the lines
for line in lines:
	# Parse the line into variables for easy comparisons
	min, max, letter, password = re.search(r'^(\d+)-(\d+) (\w): (.*)$', line).groups()

	# Decide if password passes test and increment counter
	if password.count(letter) >= int(min) and password.count(letter) <= int(max): count = count + 1

print(count)

# Reset counter
count = 0

# Iterate over the lines
for line in lines:
	# Parse the line into variables for easy comparisons
	min, max, letter, password = re.search(r'^(\d+)-(\d+) (\w): (.*)$', line).groups()

	# Decide if password passes test and increment counter
	# ^ is the bitwise XOR operator.  One condition or the other, but not both.
	if (password[int(min)-1] == letter) ^ (password[int(max)-1] == letter): count = count + 1

print(count)