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

# Recursive function for counting orbits
def count(objects, name):
    # If this object doesn't have a parent, return 0 orbits below it
    if name not in objects:
        return 0
    # Otherwise add 1 to the count and move positions
    else:
        return 1 + count(objects, objects[name])

# Iterate through objects and return the sum of the orbit counts
sum([count(objects, name) for name in objects])
