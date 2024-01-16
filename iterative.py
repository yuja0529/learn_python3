# 나동빈 파이썬 입문자 초급 강의
# _*_ coding: utf-8 _*_

#반복문: 조건에 부합하는 한 특정한 명령어를 반복
# 숫자 범위 표현: range(시작, 끝-1)

sum = 0
for i in range(1,10):
    print(i)
    sum = sum + i
print("합계",sum)

count = 0
for i in "Hello World":
    if i == "o":
        count = count + 1
print("o의 갯수는?",count,"입니다")

sum2 = 0
list = [1, 2, 3, 4, 5]
for i in list:
    sum2 = sum2 + i
print("합계",sum2)

# continue  를 만났을 때 더이상 명령어를 실행하지않고 다음 반복을 진행
# break     를 만나면 반복문을 벗어난다.

sum3 = 0
for i in list:
    if i % 2 == 1:
        continue
    sum3 = sum3 + i
print(sum3)

sum4 = 0
for i in list:
    if i % 2 == 1:
        break
    sum4 = sum4 + i
print(sum4)

i = 0
sum5 = 0
while i < 5:
    i = i + 1
    if i % 2 == 1:
        continue
    sum5 = sum5 + i
print(sum5)