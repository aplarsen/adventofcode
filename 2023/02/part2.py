import re
from functools import reduce

powers = []

with open('input.txt') as f:
    for line in f:
        minimums = {}

        id, games = re.search( r'Game (\d+): (.*)', line ).groups()

        for game in games.split(';'):
            game = game.strip()

            for subset in game.split(','):
                count, color = re.search( '(\d+) (\w+)', subset ).groups()

                minimums[color] = max( [minimums.get(color, 0), int(count)] )

        powers.append( reduce(lambda a, b: a*b, minimums.values()) )

print(powers)

print(sum(powers))