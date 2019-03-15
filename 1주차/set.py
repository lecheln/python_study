# set is unordered, not allow overlap
s1 = set([1,2,3])               # {1,2,3}
s2 = set("hello")               # {'e','h','l','o'}

# how to indexing
s1 = set([1,2,3])
li = list(s1)                   # [1,2,3]

# intersection, difference, sum of set
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s1 & s2 or s1.intersection(s2)  # {4, 5, 6}
s1 | s2 or s1.union(s2)         # {1, 2, 3, 4, 5, 6, 7, 8, 9}
s1 - s2 or s1.difference(s2)    # {1, 2, 3}
s2 - s1 or s2.difference(s1)    # {8, 9, 7}

# add set
s1.add(4)                       # {1, 2, 3, 4}
s1.update([5,6,7])              # {1, 2, 3, 4, 5, 6, 7}

# remove set
s1.remove(7)                    # {1, 2, 3, 4, 5, 6}
