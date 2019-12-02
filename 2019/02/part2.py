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
    
for noun in range(0,100):
    for verb in range(0,100): 
        memory = input[:]
        memory[1] = noun
        memory[2] = verb
        
        if compute( memory )[0] == 19690720:
            print( noun,verb )
            print( 100 * noun + verb)