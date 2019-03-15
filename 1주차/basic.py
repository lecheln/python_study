# get Address
id(a)                   # in C : &a

# check a is b
a is b                  # return True or False

# copy
from copy import copy
b = copy(a) 

# swap val
a = 5
b = 6
a, b = b, a             # a = 6, b = 5

# make val
a, b = ('1','2')        # a = '1', b = '2'
(a, b) = '1', '2'       # a = '1', b = '2'
a = b = 'a'             # a = 'a', b = 'a'

# indexing
a in b or a not in b    # b.index(a)

# get size
len(a)

# get val type
type('a')               # str

# if
a and b                 # a && b
a or b                  # a || b
not a                   # !a
if ???:
    doing~~~
    doing~~~
elif ???:
    doing2!!!
else:
    doing3@@@

# conditional expression
if score >= 60:
    msg = 'good'
else:
    msg = 'bad'

>> msg = 'good' if score >= 60 else "bad"

# while
while ???:
    doing
    if fin_while:
        break;
    elif do_Next_While:
        continue;

# for
for var in list():
    doing
    if fin_for:
        break;
    elif do_Next_for:
        continue;

# get integer list
range(start, end, size)     # for(int i = start; i < end; i += size)

# List comprehension
a = [1,2,3,4]
result = []
for num in a:
     result.append(num*3)

>> result = [num * 3 for num in a]                  # [3,6,9,12]
>> result = [num * 3 for num in a if num % 2 == 0]  # [6,12]
result = [x*y for x in range(2,10)
              for y in range(1,10)]                 # for(int x = 2; x < 10; x++) for(int y = 1; y < 10; y++) a.append(x*y)

# getInput
a = input()
a = int(input())            # get int
a, b = map(int, input().split())    

# print
print("life" "is" "short") is print("life"+"is"+"short")
print("life","is","short") is print("life is short")
print('a', end=' ')         # default is \n
