# Initialize blank dict of objects
objects = {}

# Read file
with open("input.txt", "r") as f:
    # Iterate through lines
    for line in f:
        # Split line into parent and object
        parent, name = line.rstrip().split(")")
        
        # Set name, parent in dict
        objects[name] = parent

# Recursive function for listing orbits transfers
def transfers(objects, name):    
    if name not in objects:
        return []
    else:
        return [objects[name]] + transfers(objects, objects[name])

# Initialize blank list of travel distances
matches = []

# Iterate through orbit transfers starting from SAN
for i, io in enumerate(transfers(objects, 'SAN')):
    # Iterate through orbit transfers starting from YOU
    for j, jo in enumerate(transfers(objects, 'YOU')):
        # Check if objects have same name
        if io == jo:
            # Add this set of orbit jumps to our list
            matches.append( (i,j) )
            break

# Find shortest sum of the two path lengths
min(list(map(sum, matches)))
