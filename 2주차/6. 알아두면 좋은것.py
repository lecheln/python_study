# yield
def generator(n):
    print("Start")
    while n < 10:
        yield n
        n += 1
    print("End")
     
if __name__ == "__main__":
    for i in generator(0):
        print(i)
        
# 위의 결과는 0~9까지 출력합니다.
# 제너레이터 : 데이터를 메모리에 담지 않고 그때그때 생성합니다.
# yield을 만나면서 함수를 반환해준다는 느낌입니다.
