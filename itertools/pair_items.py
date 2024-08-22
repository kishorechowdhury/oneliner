#pair every item next to each other sequentially

from itertools import pairwise

data = 'ABCDEF'
print(list(pairwise(data)))

'''
output:
[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')]
'''