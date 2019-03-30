# 오류가 나는경우
# ex ) 4 / 0 -> ZeroDivisionError

try:
    ...
except 발생오류 as 메세지 변수:
    ...


# 만약 오류 명을 모른다
try:
except:

# 로 사용가능

# 예외 상관없이 마무리 할때
# ex) 파일 닫기

try:
except:
finally:

# 로 사용합니다.

#여러개의 경우 동일하게 except를 여러번 사용하면 됩니다.

# 오류 회피하기
pass # 를 이용합니다.

# 에러를 강제로 발생시키기
raise 에러이름

# 에러를 정의하기
# class에서 Exception을 상속받는
