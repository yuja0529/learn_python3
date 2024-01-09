# 나동빈 파이썬 입문자 초급 강의
# _*_ coding: utf-8 _*_

a = input("작성해보세요.")     #사용자로부터 input값을 받고 a에 저장시킴
print(a)                     #결과: 작성한 값

# 3 + 7 = 10
a = input("숫자 두개를 작성하세요").split(" ")
# a = ['3','7']
x = int(a[0])
y = int(a[1])
print("x + y =",x + y)      #결과: x + y = 10
print("x - y =",x - y)
print("x * y =",x * y)
print("x // y =",x // y)