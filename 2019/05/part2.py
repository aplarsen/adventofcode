def compute(program, input):        
    # Start with the first position
    pos = 0
    
    # Loop forever
    while True:
        # Zero pad a string version of the instruction and gets the last two chars as an opcode
        opcode = f'{program[pos]:05d}'[-2:]                
        
        # Halt instruction
        if opcode == '99':
            return
        
        # Get list of modes from left digits.  Reverse the list so it's in the same order as the params.
        modes = f'{program[pos]:05d}'[0:-2][::-1]        
                
        # Create blank dict of params
        params = {}
        
        # Iterate through params 1-3
        for i in range(1,4):
            # Catch walking off the end of the program
            try:
                # Position mode
                if modes[i-1] == '0':
                    params[i] = program[ program[pos+i] ]
                # Immediate mode
                elif modes[i-1] == '1':
                    params[i] = program[pos+i]
            except:
                pass
        
        # Addition instruction
        if opcode == '01':
            program[ program[pos+3] ]  = params[1] + params[2]
            pos += 4
        # Multiplication instruction
        elif opcode == '02':
            program[ program[pos+3] ]  = params[1] * params[2]
            pos += 4
        # Simple save instruction
        elif opcode == '03':
            program[ program[pos+1] ] = input
            pos += 2
        # Output instruction
        elif opcode == '04':
            print( params[1] )        
            pos += 2
        # Jump-if-true instruction
        elif opcode == '05':
            if params[1] != 0:
                pos = params[2]
            else:
                pos += 3
        # Jump-if-false instruction
        elif opcode == '06':
            if params[1] == 0:
                pos = params[2]
            else:
                pos += 3  
        # Less than instruction
        elif opcode == '07':            
            program[ program[pos+3] ] = 1 if params[1] < params[2] else 0            
            pos += 4 
        # Equals instruction
        elif opcode == '08':
            program[ program[pos+3] ] = 1 if params[1] == params[2] else 0
            pos += 4            
                
# Read in program
with open('program.txt', 'r') as f:
     program = list(map(int, f.read().split(",")))

# Execute program
compute( program, 5 )
