### sys 모듈
import sys

# 시작할때 매개변수를 받는법
# sys.argv에 저장됩니다.
print(sys.argv)

# 강제로 종료하기
sys.exit()

# 내가 만든 모듈 불러오기
sys.path
sys.path.append()


### pickle 모듈
import pickle

# 객체를 그대로 저장하는법
pickle.dump(객체, 파일)
pickle.load(파일)         # 객체로 반환


### os 모듈
import os

# 환경변수를 알고 싶을때
os.environ()

# 디렉터리 위치 변경하기 (cd명령어)
os.chdir()

# 디렉터리 위치 받기 (chdir)
os.getcwd()

# 시스템 명령 호출하기
os.system()

# 디렉터리를 생성하기
os.mkdir(name)

# 디렉터리 샂게하기 (디렉터리가 비어야함)
os.rmdir(name)

# 파일을 지운다
os.unlink(name)

# 이름 바꾸기
os.rename(src, dst)



### shutil 모듈
import shutil

# 파일을 복사하는 방법
shutil.copy(src, dst)



### glob 모듈
import glob

# 폴더안에 있는 파일 읽어오는법
glob.glob(폴더)



### time 모듈
import time

# 현재시간을 실수형식으로 리턴하는 함수 (기준점 1970/1/1)
time.time()

# 실수값을 읽기 쉽게 반환 (구조체)
time.localtime(time.time())

# 더 보기 쉽게 반환
time.asctime(time.localtime(time.time()))

# 간단하게 현재시간 알아오기
time.ctime()

# 시간 지연시키기, 1 = 1
time.sleep()



### random 모듈
import random

# 0~1사이의 난수값
random.random()

# src부터 dst(미만)까지 사이중 랜덤 반환
random.randint(src, dst)

# 리스트 섞기
random.shuffle(리스트)


## numpy : http://pythonstudy.xyz/python/article/402-numpy-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

## 표준 함수 : https://docs.python.org/ko/3/library/index.html

## deciaml : https://docs.python.org/ko/3/library/decimal.html
