# 파일 입출력
f = open("파일이름", '타입') # r = 읽기, w = 쓰기, a = 추
f.close()

# 파일 쓰는법
f.write("내용")

# 파일 읽는법

# 한줄 읽
f.readline()

while True:
    line = f.readline()
    if not line: break

# 전체 읽어오기 (리스트로 가져옵니다)
lines = f.readlines()

# 전체 문장으로 가져오기
data = f.read()

# close()없이 쓰는방법!
with open("파일이름", '타입') as f:
    f.행할 행동
