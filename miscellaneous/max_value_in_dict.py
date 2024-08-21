#find item with max value in a dictionary

inventory = {'chilli': 25, 'brinjal': 32, 'potato': 26, 'onion': 62}
max_item = max(inventory, key=inventory.get)

print(f'Max number of item is {max_item} having {inventory.get(max_item)} count')

'''
Max number of item is onion having 62 count
'''