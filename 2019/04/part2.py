# Initialize an empty list of possible passwords
passwords = []

# Iterate through the input range
# Convert to a string here because we have no use for it as an int
for x in [ str(x) for x in range(367479,893698+1) ]:    
    # Assume we do not have a doubled digit
    double = False
    
    # Assume the numbers are increasing
    increasing = True
    
    # Iterate through the digits in the current password
    for pos in range(0,len(x)-1):        
        # Find left bound for a different number
        for left in range(pos-1,-2,-1):            
            if left < 0 or x[left] != x[pos]: break        
        
        # Find right bound for a different number
        for right in range(pos+1,len(x)+1):
            if right > len(x)-1 or x[right] != x[pos]: break
        
        # Compute length of this span of similar digits
        if (right-1) - (left+1) + 1 == 2:            
            double = True
        
        # Check for decreasing digit.  Break for loop if decreasing.
        if x[pos+1] < x[pos]:
            increasing = False
            break
    
    # If both conditions are met, add it to the list
    if double and increasing: passwords.append(x)

# Count length of possible passwords
len(passwords)