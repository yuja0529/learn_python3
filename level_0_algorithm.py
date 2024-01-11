# 나동빈 파이썬 입문자 초급 강의 - 백준알고리즘
# _*_ coding: utf-8 _*_

#문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

#입력: 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# ex: 1 2

#출력: 첫째 줄에 A+B를 출력한다.
# ex: 3

a = input().split(" ")
print(int(a[0]) + int(a[1]))

#========================================================================================#

#문제: 준하는 사이트에 회원가입을 하다가 joonas라는 아이디가 이미 존재하는 것을 보고 놀랐다.
# 준하는 놀람을 ??!로 표현한다. 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어졌을 때,
# 놀람을 표현하는 프로그램을 작성하시오.

#입력: 첫째 줄에 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어진다.
# 아이디는 알파벳 소문자로만 이루어져 있으며, 길이는 50자를 넘지 않는다.
# ex: joonas

#출력: 첫째 줄에 준하의 놀람을 출력한다. 놀람은 아이디 뒤에 ??!를 붙여서 나타낸다.
# ex: joonas??!

a = input()
x = "??!"
print(a+x)

#========================================================================================#

#문제: ICPC Bangkok Regional에 참가하기 위해 수완나품 국제공항에 막 도착한 팀 레드시프트 일행은 눈을
# 믿을 수 없었다. 공항의 대형 스크린에 올해가 2562년이라고 적혀 있던 것이었다. 불교 국가인 태국은 불멸기원,
# 즉 석가모니가 열반한 해를 기준으로 연도를 세는 불기를 사용한다. 반면, 우리나라는 서기 연도를 사용하고 있다.
# 불기 연도가 주어질 때 이를 서기 연도로 바꿔 주는 프로그램을 작성하시오.

#입력: 서기 연도를 알아보고 싶은 불기 연도 y가 주어진다. (1000 ≤ y ≤ 3000)
# ex: 2541

#출력: 불기 연도를 서기 연도로 변환한 결과를 출력한다.
# ex: 1998

a = int(input())
print(a-543)

#========================================================================================#

#문제: (A+B)%C는 ((A%C) + (B%C))%C 와 같을까? (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

#입력: 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
# ex: 5 8 4

#출력: 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
# ex:   1
#       1
#       0
#       0

answer = input().split(" ")                 #내가 시도한 방법
A = int(answer[0])
B = int(answer[1])
C = int(answer[2])

A,B,C = map(int, input().split((" ")))      #좀 더 효율적인 방법

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

#========================================================================================#

#문제: (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)
# 위치에 들어갈 값을 구하는 프로그램을 작성하시오.

#입력: 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
# ex: 472
#     385

#출력: 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.
# ex: 2360
#     3776
#     1416
#     181720

#풀이: 두번째줄에 받아오는 자연수는 문자열로 받아서 index값을 이용한다
#     472 * 마지막자릿수(5)를 하면 2360,
#     472 * 두번째자릿수(8)을 하면 3776,
#     472 * 첫번째자릿수(3)을 하면 1416이 됨


a = int(input())                    #내가 시도한 방법
b = input()
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))

a = int(input())                    #반복문을 사용한 좀 더 짧은 방법
b = input()
for i in range(3, 0, -1):
    print(a * int(b[i - 1]))
print(a * int(b))

#========================================================================================#

#문제: 꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!

#입력: 첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 1012)이 공백을 사이에 두고 주어진다.
# ex: 77 77 7777

#출력: A+B+C의 값을 출력한다.
# ex: 7931

a,b,c = map(int, input().split((" ")))
print(a+b+c)

#========================================================================================#