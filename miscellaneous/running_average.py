#find running average from a dynamic list of numbers

def mean():
    numbers = []
    def wrapper(number):
        numbers.append(number)
        
        return sum(numbers) / len(numbers)
    
    return wrapper

sample_mean = mean()
print(sample_mean(100))
print(sample_mean(105))
print(sample_mean(101))
print(sample_mean(98))

'''
output:
100.0
102.5
102.0
101.0
'''