#example of set operations: union, intersection, difference, symmetric difference

s1 = {1, 2, 3}
s2 = {3, 4, 5}

# numbers in a or b or both
print(f'union: {s1 | s2}')

# numbers in both a and b
print(f'intersection: {s1 & s2}')

# numbers in a but not in b
print(f'difference: {s1 - s2}')

# numbers in a or b but not both
print(f'symmetric difference: {s1 ^ s2}')