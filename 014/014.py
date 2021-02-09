list_1 = [1,5,7,9]
list_2 = [2,2,6,8]

result = list_1 + list_2

result.sort()

print(f'merge result {result}')


list_1 = [1,5,7,9]
list_2 = [2,2,6,8]

list_1.extend( list_2 )
list_1.sort()

print(f'merge result {list_1}')