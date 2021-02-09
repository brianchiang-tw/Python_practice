# sort

sequence = [1, 3, 5, 4, 2, 6]
# Original Sequence [1, 3, 5, 4, 2, 6]
print(f'Original Sequence', sequence)

sequence.sort()
# After sorting [1, 2, 3, 4, 5, 6]
print(f'After sorting', sequence)



# sorted

sequence = [1, 3, 5, 4, 2, 6]
output = sorted(sequence)

print(f'Original Sequence', sequence)
print(f'Output sequence after sorting', output)
print(f'Original sequence after sorting', sequence)



test_list = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
print(sorted(test_list, key=lambda x:x['age'], reverse=True))