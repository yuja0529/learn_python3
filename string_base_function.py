# 나동빈 파이썬 입문자 초급 강의
# _*_ coding: utf-8 _*_

a = "안녕"
b = "파이썬"
print(a+b)      #결과: 안녕파이썬
print((a+b)*5)  #결과: 안녕파이썬안녕파이썬안녕파이썬안녕파이썬안녕파이썬

c = "Hello World"
print(c[0])     #결과: H
print(c[-3])    #결과: r

print(c[2:9])   #시작은 0부터 끝자리는 0+1로 계산
                #결과: llo Wor

print(c[2:])    #2부터 끝까지 출력
                #결과: llo World

print(c[:-2])   #뒤에있는 단어 2개만 빼고 출력
                #결과: Hello Wor

print(c[0:7:2]) #0부터 7번째 자리까지 2번건너뛴 문자열을 출력
                #결과: HloW

#====================================================================================#

print(c.replace("Hello","Hi"))  #대소문자가 같은 Hello를 Hi라는 문자열로 대체
                                            #결과: Hi World

print(c.count("r"))     #c변수에서 r이 몇번이나 쓰였는지 셀수있는 함수
                        #결과: 1

print(c.find("Wor"))    #c변수에서 해당단어 시작 index위치 반환
                        #결과: 6

print(c.lower())        #문자열 전체를 소문자로 변환
                        #결과: hello world

print(c.upper())        #문자열 전체를 대문자로 변환
                        #결과: HELLO WORLD

print(c.strip("Hello "))#c변수에서 Hello 라는 문자열을 지움
                        #결과: World

print(c.split(" "))     #문자열을 파리미터 기준으로 배열로 나눔
                        #결과: ['Hello', 'World']

print(c.zfill(20))      #빈자리를 0를 처리해줌
                        #결과: 000000000Hello World

a = "4503"
b = int(a)              #문자열인 숫자를 숫자로 변환
print(b+505)            #결과: 5008

#====================================================================================#

print("\n")             #줄바꿈
print("\t")             #수평 탭(tab)
print("\\")             #\
print("\"")             #""
print("\'")             #''