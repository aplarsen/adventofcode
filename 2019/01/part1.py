import pandas as pd

input = pd.read_csv("input.txt")

input['fuel'] = input['mass'] // 3 - 2

input.aggregate(func=sum)