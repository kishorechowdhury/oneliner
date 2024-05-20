# Python provides convenience functions to make accessor functions easier and faster. 
# The operator module has itemgetter() which is used for this situation.
# The operator module functions allow multiple levels of sorting. For example, to sort by grade then by age:


from operator import itemgetter

student_tuples = [
    ('sanjay', 'A', 16),
    ('vijay', 'B', 17),
    ('ajay', 'B', 15),
]
print(sorted(student_tuples, key=itemgetter(1, 2)))


'''
output:
[('sanjay', 'A', 16), ('ajay', 'B', 15), ('vijay', 'B', 17)]
'''