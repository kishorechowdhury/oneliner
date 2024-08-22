#visit input iterables in a cycle until each is exhausted in a roundrobin manner

from itertools import cycle, islice

def roundrobin(*iterables):
    # Algorithm credited to George Sakkis
    iterators = map(iter, iterables)
    for num_active in range(len(iterables), 0, -1):
        iterators = cycle(islice(iterators, num_active))
        yield from map(next, iterators)

print(list(roundrobin('ABC', 'D', 'EF')))
 
'''
output:
['A', 'D', 'E', 'B', 'F', 'C']
'''