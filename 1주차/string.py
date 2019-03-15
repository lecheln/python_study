# type of string
"hello world"
'hello world'
'''hello world'''
"""hello world"""

# why use ''' or """"
string = '''
hello
world
'''
string = """
hello
world
"""

# escape char
# \n	개행 (줄바꿈)
# \t	수평 탭
# \\	문자 "\"
# \'	단일 인용부호(')
# \"	이중 인용부호(")
# \000	널문자

# string concatenation
head = 'life'
tail = ' is short'
head + tail                                 # 'life is short'

# string mul
head = 'haha'
head * 2                                    # 'hahahaha'
print('=' * 20)                             # '===================='

# string length
a = 'life is too short'
len(a)                                      # 17

# string indexing
a = 'Life is too short, You need Python'
a[3]                                        # 'e'
a[-1]                                       # n // reverse indexing

# string sliceing
a = 'Life is too short, You need Python'
b = a[0:4]                                  # 'Life'
b = a[:]                                    # 'Life is too short, You need Python'
b = a[19:]                                  # 'You need Python'
b = a[:17]                                  # 'Life is too short'
b = a[19:-7]                                # 'You need'

# Notice
a = 'Life is too short, You need Python'
a[0] = 'a'                                  # error, python string is immutable
a = 'a' + a[1:]                             # 'aife is too short, You need Python'

# string formating
'test %d' % 5                               # 'test 5'
'test %s' % 'ha'                            # 'test ha'
'test case %d : %s' (2,'test')              # 'test case 2 : test'

# use format function
'test {0}'.format(5)                        # 'test 5'
'test {0}'.format('ha')                     # 'test ha'
'test case {0} : {1}'.format(2,'test')      # 'test case 2 : test'
'test case {a} : {b}'.format(a=2,b='test')  # 'test case 2 : test'
'{0:<10}'.format('test')                    # 'test      '
'{0:>10}'.format('test')                    # '      test'
'{0:^10}'.format('test')                    # '   test   '
'{0:+^10}'.format('test')                   # '+++test+++'
'{0:.4f}'.format(1.23456789)                # '1.2345'
'{0:05d}'.format(12))                       # '00012'
'test {{0}}'.format(5)                      # 'test {0}'

# count string
a = 'test'
a.count(t)                                  # 2

# find string
a = 'test'
a.find('t')                                 # 0
a.find('a')                                 # -1
a.index('t')                                # 0
a.index('a')                                # error

# join string
",".join("test")                            # 't,e,s,t'
",".join(['a','b','c','d'])                 # 'a,b,c,d'

# upper, lower string
'hi'.upper()                                # 'HI'
'HI'.upper()                                # 'hi'

# delete space
a = ' hi '
a.lstrip()                                  # 'hi '
a.rstrip()                                  # ' hi'
a.strip()                                   # 'hi'

# replace string
a = 'life is too short'
a.replace('short','zero')                   # 'life is too zero'

# split string
a = 'life is too short'
a.split()                                   # ['life','is','too','short']
a.split(' ')                                # ['life','is','too','short']

# fill string
'3'.zfill(4)                                # '0003'
'3'.rjust(4,'1')                            # '1113'

 