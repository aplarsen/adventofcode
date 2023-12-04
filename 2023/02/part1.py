import re

#The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

criteria = {
    'red': 12,
    'green': 13,
    'blue': 14
}

possible_games = []

with open('input.txt') as f:
    for line in f:
        id, games = re.search( r'Game (\d+): (.*)', line ).groups()

        possible = True

        for game in games.split(';'):
            game = game.strip()

            for subset in game.split(','):
                count, color = re.search( '(\d+) (\w+)', subset ).groups()

                if int(count) > criteria[color]:
                    possible = False

        if possible:
            possible_games.append( id )

print(possible_games)

print( sum(map(int, possible_games)))