# 정수형
a = 1

# 소수점
a = 1.4
a = 7.25E10             # 7.25 * 10^10
a = 4.95e-10            # 4.95 * 10^-10

# 2진법, 8진법, 16진법
# 2진법은 0b로시작한다.
# 8진법은 0o, 0O로 시작한다. (숫자0 다음에 영어 o)
# 16진법은 0x, 0X로 시작한다.
a = 0b110               # 6
a = 0o06                # 6
a = 0xa                 # 10

# 2진법, 8진법, 16진법으로 변환하는 방법.
# 숫자에서 문자열로 변환해준다.
a = bin(6)              # '0b110'
a = oct(10)             # '0o12'
a = hex(10)             # '0xa'

# 2진법, 8진법, 16진법 문자열을 숫자로 변환하는법
# 문자열을 넣고, 다음 파라메터에 몇진수인지 적는다.
a = int('0b110',2)      # 6
a = int('0o6',8)        # 6
a = int('0xa',16)       # 10

# 사칙연산
# c언어와 비슷하지만, 다른점은 /를 할때 정수로 나눠지지 않는다.
a = 5
b = 2
a + b                   # 7
a - b                   # 3
a * b                   # 10
a / b                   # 2.5

# 거듭제곱 하는방법
a ** b                  # 25 (5 ^ 2)

# 나머지 구하기
a % b                   # 1

# 몫 구하기
a // b                  # 2

# 허수
# 실제적으로 사용할 일은 거의 없지만, 실수부는 real, 허수부는 imag, 켤레 복소수는 conjugate()로 알수 있다.
a = 2 + 3j              # 2 + 3i
a.real                  # 2.0
a.imag                  # 3.0
a.conjugate()           # 2 - 3i

# 수학에 필요한 기본함수
# 내장되어 있는 함수이다.
round()                 # 반올림
abs()                   # 절대값

# c언어로 치면 math.h에 해당되는 모듈
# 선언법은 import 묘듈
import math
# 사용법은 math.함수이름이다.
math.pi                 # 3.141592.....
math.e                  # 2.7182818...., 자연상수
math.trunc()            # 내림
math.factorial(n)       # 펙토리얼
math.degress()          # rad -> degress
math.radians()          # degress -> rad
# cos(),sin(),tan(),acos(),asin(),atan() # 삼각함수
math.pow(a,b)           # a ^ b 거듭제곱
math.sqrt(a)            # root a 루트
math.log(a,b)           # log b a // default = e 로그
math.log10(a)           # log10 a 로그
