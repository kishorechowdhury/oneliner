text = 'A is a but B is not a'
print(sorted(text.split(), key=str.casefold))


'''
output:
['A', 'a', 'a', 'B', 'but', 'is', 'is', 'not']
'''