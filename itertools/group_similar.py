#group similar values from a given list of values

from itertools import groupby

data = [{'name': 'Ajay', 'age': 34},
        {'name': 'Vijay', 'age': 34},
        {'name': 'Ram', 'age': 29},
        {'name': 'Shyam', 'age': 33}]
        
grouped_data = groupby(data, lambda x: x['age'])
for key, group in grouped_data:
    print(f'{key}: {list(group)}')

'''
output:
34: [{'name': 'Ajay', 'age': 34}, {'name': 'Vijay', 'age': 34}]
29: [{'name': 'Ram', 'age': 29}]
33: [{'name': 'Shyam', 'age': 33}]
'''