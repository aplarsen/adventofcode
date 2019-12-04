# Read file into list of instructions
wires = []
with open("input.txt", "r") as f:
    wires = [{"instructions": line.rstrip().split(",")} for line in f]

# Set the starting point for traversing the grid
origin = (0,0)

# Iterate through the two wires
for wire in wires:
    # Set first pair to the origin
    wire['pairs'] = [ origin ]
    
    # Iterate through instructions for this wire
    for instruction in wire['instructions']:
        
        # Split instruction into a direction (first character) and distance (the numbers)
        dir = instruction[0]
        dist = int(instruction[1:])
        
        # Create a vector to transform a position in the left-right (0) and up-down (1) directions
        if dir == 'R': vector = ( 1,  0)
        if dir == 'L': vector = (-1,  0)
        if dir == 'U': vector = ( 0,  1)
        if dir == 'D': vector = ( 0, -1)
        
        # Loop dist times
        for x in range(0, dist):
            # Apply the vector to our current position
            pair = tuple(map(lambda x,y: x+y, wire['pairs'][-1], vector))
            
            # Store the new position in our list of ordered pairs
            wire['pairs'].append( pair )

# Create lists of hashes to make searching faster
wire1 = list(map(hash, wires[0]['pairs']))
wire2 = list(map(hash, wires[1]['pairs']))

# Build a list of hashes found in both sets
hashes = [value for value in wire1 if value in wire2][1:]
hashes

# Build a list of intersections by finding ones that hash to the hashes we found earlier
intersections = [value for value in wires[0]['pairs'] if hash(value) in hashes]
intersections

# Compute Manhattan distances
manhattans = list(map(lambda x: abs(x[0]-origin[0]) + abs(x[1]-origin[1]), intersections))
manhattans

# Find the minimum Manhattan distance
min(manhattans)