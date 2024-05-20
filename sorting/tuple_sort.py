student_tuples = [
    ('sanjay', 'A', 16),
    ('vijay', 'B', 17),
    ('ajay', 'B', 15),
]
print(sorted(student_tuples, key=lambda student: student[2]))