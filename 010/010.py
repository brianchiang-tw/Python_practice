def print_element( container ):

    if type(container) == type( dict() ):

        for k, v in container.items():
            print(f'{k} -> {v}', end = ',')
    
    else:
        for element in container:
            print(f'{element}', end = ',')



test_list = [4,2,3,1,4]
test_tuple = (5,2,1,3,4)
test_dict = {'a':1, 'b':2}
test_set = {12,4,6,5}


print('\nlist')
print_element(test_list)
print()

print('\ntuple')
print_element(test_tuple)
print()

print('\ndict')
print_element(test_dict)
print()

print('\nset')
print_element(test_set)
print()