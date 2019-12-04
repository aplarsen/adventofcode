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
        # Check for doubled digit
        if x[pos] == x[pos+1]: double = True
        
        # Check for decreasing digit.  Break for loop if decreasing.
        if x[pos+1] < x[pos]:
            increasing = False
            break
    
    # If both conditions are met, add it to the list
    if double and increasing: passwords.append(x)

# Count length of possible passwords
len(passwords)