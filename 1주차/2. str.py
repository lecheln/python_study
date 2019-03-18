# 문자열의 종류
"hello world"
'hello world'
'''hello world'''
"""hello world"""

# 어째서 ''', """를 사용할까?
string = '''
hello
world
'''
string = """
hello
world
"""
# 다음 예제와 같이 여러줄을 사용하기 위해서 사용한다.

# escape char
# c언어랑 동일하다
# \n	개행 (줄바꿈)
# \t	수평 탭
# \\	문자 "\"
# \'	단일 인용부호(')
# \"	이중 인용부호(")
# \000	널문자

# 문자열 합치기
head = 'life'
tail = ' is short'
head + tail                                 # 'life is short'

# 문자열 곱하기
head = 'haha'
head * 2                                    # 'hahahaha'
print('=' * 20)                             # '===================='

# 문자열 길이 구하기
a = 'life is too short'
len(a)                                      # 17

# 문자열 인덱싱
# c언어의 문자열 참조와 같다.
# 하지만 음수부를 씀으로써 뒤에서부터 접근할 수 있다.
a = 'Life is too short, You need Python'
a[3]                                        # 'e'
a[-1]                                       # n // reverse indexing
a[3] = 'a'                                  # error
# 파이썬의 문자열은 수정이 불가능하다. 그래서 수정하기 위해, 문자열을 자르거나 교체를 한다.

# 문자열 자르기
a = 'Life is too short, You need Python'
b = a[0:4]                                  # 'Life'
b = a[:]                                    # 'Life is too short, You need Python'
b = a[19:]                                  # 'You need Python'
b = a[:17]                                  # 'Life is too short'
b = a[19:-7]                                # 'You need'
a = a[::-1]                                 # 'nohtyP deen uoY ,trohs oot si efiL"
# 문자열[시작점:끝나는점:진행값]을 통해 원하는 대로 자를 수 있다. 진행값은 없어도 괜찮다. default = 1
# 시작점을 안적는 경우 자동으로 0으로 지정된다.
# 끝점을 안적을 경우 자동으로 맨 끝이 지정된다.

# 문자열 수정하는 방법
a = 'Life is too short, You need Python'
a = 'l' + a[1:]                             # 'life is too short, You need Python'

# 문자열 포멧팅
# c언어의 printf랑 비슷하다. 다만 c언어에서는 "문자열", 변수~~ 였던것이
# 파이썬에서는 "문자열" % (변수~~~) 로 변경되었다.
'test %d' % 5                               # 'test 5'
'test %s' % 'ha'                            # 'test ha'
'test case %d : %s' (2,'test')              # 'test case 2 : test'

# 포멧 함수를 사용하는 방법
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
# 위의 예제와 같이 {} 이 안에 지정된 형식, 번호 혹은 이름을 넣음으로써 지정한다


# 문자열 안에 있는 문자 갯수 구하기
a = 'test'
a.count(t)                                  # 2

# 문자 찾기
# find함수의 경우 못찾으면 -1을 반환하지만, index함수의 경우 error를 반환해 프로그램이 종료된다.
a = 'test'
a.find('t')                                 # 0
a.find('a')                                 # -1
a.index('t')                                # 0
a.index('a')                                # error

# 문자열 합치기
# 대부분 다음장에 배우는 리스트를 합칠때 자주 사용한다.
",".join("test")                            # 't,e,s,t'
",".join(['a','b','c','d'])                 # 'a,b,c,d'

# 문자열 대문자, 소문자로 바꾸기
'hi'.upper()                                # 'HI'
'HI'.lower()                                # 'hi'

# 좌우로 있는 공백 지우기
a = ' hi '
a.lstrip()                                  # 'hi '
a.rstrip()                                  # ' hi'
a.strip()                                   # 'hi'

# 문자열 교체하기
a = 'life is too short'
a.replace('short','zero')                   # 'life is too zero'

# 문자열 자르기
a = 'life is too short'
a.split()                                   # ['life','is','too','short']
a.split(' ')                                # ['life','is','too','short']

# 문자열 채우기
# zfill = zerofill
'3'.zfill(4)                                # '0003'
'3'.rjust(4,'1')                            # '1113'

# 알파벳으로만 이루어져있는지 확인하기
'asdf'.isalpha()                            # True

# 알파벳과 숫자로만 이루어져있는지 확인하기
'asdf2314'.isalnum()                        # True

# 문자열이 대문자, 소문자로 이루어져있는지 확인하는 방법
'hi'.isupper()                              # False
'HI'.islower()                              # False
