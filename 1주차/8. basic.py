# 변수의 주소값 찾기
id(a)                   # in C : &a

# 동일한지 확인하는 방법
a is b                  # return True or False

# 복사하는 방법
# 파이썬에서 리스트 복사의 경우 서로 동일한 객체가 된다
# 그렇기에 b = a[:]나 copy함수를 이용해 복사한다.
from copy import copy
b = copy(a) 

# 두 변수를 서로 바꾸는 방법
a = 5
b = 6
a, b = b, a             # a = 6, b = 5

# 변수 선언하는 방법
a, b = ('1','2')        # a = '1', b = '2'
(a, b) = '1', '2'       # a = '1', b = '2'
a = b = 'a'             # a = 'a', b = 'a'

# 인덱싱 할 객체(b)가 a에 있는지 확인하는 방법
a in b
a not in b    # b.index(a)

# 크기 구하기
len(a)

# 타입 알아내는 방법
type('a')               # str

# if 조건문
# c언어와 달리 &&, ||, !를 영어로 사용한다.
# else if 의 경우 elif로 사용한다
# 파이썬은 4칸 들여쓰기를 권장하고 있지만, tab키를 통한 8칸 들어쓰기도 상관없다.
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

# 삼항연산자
if score >= 60:
    msg = 'good'
else:
    msg = 'bad'

msg = 'good' if score >= 60 else "bad"

# while문
# c언어와 동일하다.
while ???:
    doing
    if fin_while:
        break;
    elif do_Next_While:
        continue;

# for문
# c의 for문보다 c++이나 c#의 foreach문과 비슷하다.
# 이 부분은 직접 경험해보는 것이 가장 빠르다.
# for i in "str"
#    print(i)           # 의 결과는 s t r이 나온다.
for var in list():
    doing
    if fin_for:
        break;
    elif do_Next_for:
        continue;

# 숫자 리스트 가져오는 방법
# start값은 없을경우 0으로 지정된다.
# size는 없는 경우 기본 1으로 지정된다.
range(start, end, size)     # for(int i = start; i < end; i += size)

# List comprehension
# 고급 기술입니다.
# 알아두셔도 좋고 모르셔도 괜찮습니다.
a = [1,2,3,4]
result = []
for num in a:
     result.append(num*3)

>> result = [num * 3 for num in a]                  # [3,6,9,12]
>> result = [num * 3 for num in a if num % 2 == 0]  # [6,12]
result = [x*y for x in range(2,10)
              for y in range(1,10)]                 # for(int x = 2; x < 10; x++) for(int y = 1; y < 10; y++) a.append(x*y)

# 입력 받는 방법
a = input()
a = int(input())            # get int
a, b = map(int, input().split())    

# 출력하는 방법
print("life" "is" "short") is print("life"+"is"+"short")
print("life","is","short") is print("life is short")
# 한줄에 다 출력하고 싶을때에는 end='끝마침'을 통해 지정할 수 있다.
print('a', end=' ')         # default is \n
