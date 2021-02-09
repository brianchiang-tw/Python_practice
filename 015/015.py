sequence = 'Hello World'

# expected output:
# dlroW olleH
for char in reversed(sequence):
    
    print(char, end='')

print()

# expected output:
# dlroW olleH
for idx in range(len(sequence)-1, -1, -1):

    char = sequence[idx]
    print(char, end='')

print() 

# expected output:
# dlroW olleH
for char in sequence[::-1]:

    print(char, end='')


print()

char_list = list(sequence)
char_list.reverse()

# expected output:
# dlroW olleH
for char in char_list:

    print(char, end='')




s = "Hello"

# expected output:
# olleH

print( s[::-1] )

char_list = list(s)
char_list.reverse()
print( ''.join(char_list) )

print()

s = "Hello"

# expected output:
# olleH
for i in range(0, len(s)):

    print(s[len(s)-i-1], end='')
