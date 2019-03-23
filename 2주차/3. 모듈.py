# 모듈이란 무엇인가?
# C언어에서 헤더파일과 같은 존재
import 모듈명

# 모듈안에 있는 함수 사용방법
모듈명.함수()

# 축약하는 방법
from 모듈이름 import 모듈함수

# c언어의 int main을 선언하는 방법
if __name__ == "__main__"

# 예제
# test1.py
TEST = 1.4

def printVer():
    print(str(TEST))

# test2.py
import test1
print(test1.TEST)
test1.printVer()


# 직접 만들어봅시다.
