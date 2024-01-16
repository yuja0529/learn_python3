# 나동빈 파이썬 입문자 초급 강의
# _*_ coding: utf-8 _*_

# 증감 연산자: 기존에 사용하던 증가/감소 기능을 짧게 이용
a = 10
a+= 10              #a = a + 10 과 같은뜻이다 / 파이썬에서는 ++이 사용되지 않는다
print(a)

#관계 연산자: 두개의 값을 비교하여 관계
# a == b : a와 b가 같은지 판별 => boolean값으로 표현됨
# a != b : a가 b와 다른지 판별 => boolean값으로 표현됨

b = 30
print(a == b)
print(a != b)
print(a > b)

a = "ABC"
b = "DEF"
print(a == b)
print(a < b)        #문자열은 사전순으로 비교하기 때문에 a가 b보다 사전순으로 먼저 나오기때문에 true값이 나옴

#a and b    : a와 b가 모두 참인지 판별
#a or b     : a혹은 b가 참인지 판별
#not a      : a가 거짓인지 판별

a = True
b = False
print(a and b)
print(a or b)
print(not a)