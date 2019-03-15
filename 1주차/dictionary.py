# {key1 : value1, key2 : value2, key2 : value2}
dic = {'name':'hi', 'phone':'01000000000', 'birth': '1002'}
a = { 'a': [1,2,3]}
dic = dict()

# key is immutable
# add dictionary
a = {1:'a'}
a[2] = 'b'              # {1: 'a', 2: 'b'}
a['name'] = 'pey'       # {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1,2,3]          # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
del a[1]                # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# create key List
a = {'name':'hi', 'phone':'01000000000', 'birth': '1002'}
a.keys()                # dict_keys(['name','phone','birth']) , 
                        # dict_keys is same list but append,insert,pop,remove,sort didnt work
list(a.keys())          # change dict_keys to list

# create values List
a = {'name':'hi', 'phone':'01000000000', 'birth': '1002'}
a.values()              # dict_values(['hi','01000000000','1002'])

# get key, values
a.items()               # dict_items([('name', 'hi'), ('phone', '0119993323'), ('birth', '1118')])

# delete all
a.clear()               # {}

# get values by key
a = {'name':'hi', 'phone':'01000000000', 'birth': '1002'}
a.get('name')           # 'hi'
a['name']               # 'hi'
a['test']               # error
a.get('test')           # return None
a.get('test', 'error')  # 'error'

# serach key
'name' in a             # true