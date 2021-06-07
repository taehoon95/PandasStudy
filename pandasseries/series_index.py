import pandas as pd

list_data = ['2021-06-02', 3.14, 'ABC', True]

sr = pd.Series(list_data)

print(sr)

idx = sr.index
val = sr.values

print(idx)

print('\n')

print(val)

list_index = [1, 2, 3, 4]
sc = pd.Series(list_data, index=list_index)
print(sc,sep='\n',end='\n\n')
print(type(sc.index), sc.index, sep='\n', end='\n\n')
print(type(sc.values), sc.values, sep='\n', end='\n\n')
