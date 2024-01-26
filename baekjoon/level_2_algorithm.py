# 나동빈 파이썬 입문자 초급 강의 - 백준알고리즘
# _*_ coding: utf-8 _*_

'''
문제: N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

입력: 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
ex: 2

출력: 출력형식과 같게 N*1부터 N*9까지 출력한다.
ex: 2 * 1 = 2
    2 * 2 = 4
    2 * 3 = 6
    2 * 4 = 8
    2 * 5 = 10
    2 * 6 = 12
    2 * 7 = 14
    2 * 8 = 16
    2 * 9 = 18
'''

n = int(input())
i = 0
while i < 9:
    i += 1
    print(n, "*", i, "=", n * i)

#========================================================================================#

'''
문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
ex: 5
    1 1
    2 3
    3 4
    9 8
    5 2

출력: 각 테스트 케이스마다 A+B를 출력한다.
ex: 2
    5
    7
    17
    7
'''

t = int(input())
i = 0
while i < t:
    a, b = map(int, input().split(" "))
    i += 1
    print(a + b)

# ========================================================================================#

'''
문제: n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력: 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
ex: 3

출력: 1부터 n까지 합을 출력한다.
ex: 6
'''

n = int(input())
total = 0
for i in range(1, n + 1):       #숫자 범위 표현: range(시작, 끝)
    total += i

print(total)