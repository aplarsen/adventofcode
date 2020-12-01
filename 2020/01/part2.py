import numpy

# Read lines from input.  Cast into integers.
with open("input.txt") as f:
    items = [int(x) for x in f.read().split("\n")]

# Double-loop through list
for i in range(0,len(items)):
    for j in range(i+1,len(items)):
        for k in range(j+1,len(items)):
            # Create tuple of current items
            current_items = (items[i], items[j], items[k])

            # Check for sum.a
            if numpy.sum(current_items) == 2020:

                # Print product
                print( numpy.product(current_items) )