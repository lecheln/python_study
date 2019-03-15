a = [1,2,3,4,5]
b = [1,2,[1,2]]
c = [1,'test','tset']
d = [1,'test',['tset',1]]
a = list()

# indexing list
a = [1,2,3]
a[0]                        # 1
a[0]+a[2]                   # 1 + 3 = 4
a[-1]                       # 3
a = [1,2,3,['a','b','c']]
a[3]                        # ['a','b','c']
a[3][1]                     # 'b'

# list slicing, add, mul, len is same to string

# list change
a = [1,2,3]
a[2] = 4                    # [1,2,4]

# delete list
a = [1,2,3,4,5]
del a[1]                    # [1,3,4,5]
del a[2:]                   # [1,3]

# list append
a = [1,2,3]
a.append(4)                 # [1,2,3,4]
a.append([5,6])             # [1,2,3,4,[5,6]]

# list sort
a = [1,3,2,4]
a.sort()                    # [1,2,3,4]

# list reverse
a = [1,2,3]
a.reverse()                 # [3,2,1]

# list index
a = [1,2,3]
a.index(3)                  # 2
a.index(0)                  # error

# list insert (insert(where,val))
a = [1,2,3]
a.insert(1,4)               # [1,4,2,3]

# list remove (delete first num)
a = [1,2,3,1,2,3]
a.remove(3)                 # [1,2,1,2,3]

# list pop
a = [1,2,3]
a.pop()                     # 3, a = [1,2]

# list count
a = [1,2,1,3]
a.count(1)                  # 2

# list extend
a = [1,2,3]
a.extend([4,5])             # [1,2,3,4,5] // same a += [4,5]


