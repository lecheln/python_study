# 함수를 만드는 방법
def 함수명(매개변수):
    <수행할 문장>
    return 리턴값

# 매개변수가 없어도 됨
def 함수명():
    <수행문장>
    return 리턴값

# 결과값이 없어도됨
# 이경우 None이 반환
def 함수명(매개변수):
    <수행할 문장>

# 매개변수를 지정해서 호출하는 방법
def add(a,b):
    return a+b

result = add(a=1,b=3)
result2 = add(b=1,a=3)

# 만약 매개변수가 몇개가 될지 모른다면?!
def 함수이름(*매개변수):
    <수행 문장>

# list처럼 들어가면 된다!
def sum(*args):
    result = 0
    for i in args:
        result = result + i
    return result

# 알면 좋고 몰라도되는거
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)   # {'a':1}
# 이런식으로 사전형태로 만들수있다.

# 리턴 여러개 하기
# 튜플 형태로 반환된다.
def 함수명():
    return 리턴1, 리턴2

a, b = 함수명()

# 매개변수 설정하기
def 함수이름(매개변수, 매개변수2=1):
    <수행할 문장>

함수이름(1)
함수이름(1,2)

# 무조건 외부변수를 쓰고싶다?
global a

# 람다
lambda 매개변수 : 리턴값

# 람다를 쓰는이유?
# 한줄짜리 함수일 경우 간단해진다
# def를 사용할 수 없는 곳에 쓰인다!
