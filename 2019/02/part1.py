def compute(input):    
    pos = 0
    
    while True:
        if input[pos] == 1:
            input[ input[pos + 3] ]  = input[ input[pos + 1] ] + input[ input[pos + 2] ]
        elif input[pos] == 2:
            input[ input[pos + 3] ]  = input[ input[pos + 1] ] * input[ input[pos + 2] ]
        elif input[pos] == 99:
            return input
        
        pos = pos + 4

with open('input.txt', 'r') as f:
    input = list(map( int, f.read().split(",")))     

input[1] = 12
input[2] = 2

compute(input)[0]