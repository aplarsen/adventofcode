import pandas as pd

input = pd.read_csv("input.txt")
   
def mass2fuel(mass):
    thisfuel = mass // 3 - 2

    if thisfuel > 0:
        return thisfuel + mass2fuel(thisfuel)
    else:
        return 0

input['fuel'] = list( map( lambda x: mass2fuel(x), input['mass'] ) )

input.aggregate(func=sum)