v1 = { }
v2 = { 3:5 }

# list is not hashable
# TypeError: unhashable type: 'list'
v3 = { [11,23]: 5 }
v4 = { (11,23): 5 }