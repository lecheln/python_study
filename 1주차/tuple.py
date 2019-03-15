# tuple is not delete anything

t = ()
t1 = (1,)
t2 = 1,2,3

# delete tuple?
del t2[0]       # error

# change tuple?
t2[0] = 2       # error

# slicing, indexing, add, mul, len is same to list