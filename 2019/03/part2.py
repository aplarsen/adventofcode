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

# Build a list of pairs found in both sets
intersections = set(wires[0]['pairs']).intersection(wires[1]['pairs'])
intersections.remove( (0,0) )
intersections

# Initialize an empty list of steps
steps = []

# Iterate through our found intersections
for intersection in intersections:    
    # Wire 1
    # Start with the first ordered pair
    loc1 = 0
    
    # Iterate through the ordered pairs until we find the first one that puts us at this intersection
    while wires[0]['pairs'][loc1] != intersection and loc1 < len(wires[0]['pairs'])-1:
        loc1 += 1
    
    # Wire 2
    # Start with teh first ordered pair
    loc2 = 0
    
    # Iterate through the ordered pairs until we find the first one that puts us at this intersection
    while wires[1]['pairs'][loc2] != intersection and loc2 < len(wires[1]['pairs'])-1:
        loc2 += 1        
    
    # Save these numbers of steps in a list
    steps.append( (loc1, loc2) )   

# Compute the sums of these steps
combinedsteps = list(map(sum, steps))
combinedsteps

# Find the minimum sum of these steps
min(combinedsteps)