# 나동빈 파이썬 입문자 초급 강의
# _*_ coding: utf-8 _*_

'''
첫 명령어는 들여쓰기 없이 시작해야 한다.
조건문, 반복문 등의 문법을 사용할 때는 콜론(:)으로 명령어의 끝을 알리고,
콜론(:)의 다음 줄 부터는 들여쓰기의 간격이 모두 일정해야 한다.
'''

score = 75
if score >= 80:
    print("Good")
elif score >= 70:
    print("Not Bad")
else:
    print("Bad")
print("조건문 코드블럭 밖에있는 것은 무조건 실행됩니다")

score2 = 85
if score2 < 90 and score2 >= 80:
    print("Good")

score3 = 90
if score3 == 100 or score3 == 90:
    print("Great")