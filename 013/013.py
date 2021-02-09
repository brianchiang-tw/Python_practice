alist = ['a', 'b', 'c', 'd', 'e', 'f']

blist = ['x','y','z','d','e','f']


# Method_#1

result = list( set(alist).union(blist) )
result.sort()

print(f'intersection {result}')

# Method_#2

result = alist

for element in blist:

    if element not in result:

        result.append( element )

print(f'intersection {result}')



# Method_#3

def merge_list( *args ):

    s = set()

    for element in args:
        s = s.union(element)

    return list(s)


result = merge_list(alist, blist)
result.sort()

print(f'intersection {result}')