'''
print(1+1) #2
print(2**3) #2^3 8
print(5%3) # 나머지 2
print(5//3) # 몫만  1
print(8/3) # 2.66666666666666
'''
# 'and' =='&'
# 'or'=='|'


# print (2 + 3 * 4) #14

# print(abs(-5)) #5
# print(pow(4,2)) #4^2 = 16
# print(max(5,12)) # 12
# print(min(5,12)) # 5
# print(round(3.14)) # 3 반올림
# print(round(4.99)) # 5 반올림

# from math import *
# print(floor(4.99)) # 내림
# print(ceil(3.14)) # 올림 
# print(sqrt(16)) # 제곱근

# #랜덤함수

# from random import*

# print(random()) #0.0이상 1.0 미만의 임의의 값 생성

# print(int(random()* 10)) #0~10미만의 임의의 값 
# print(randrange(1,46)) # 1~46미만
# print(randint(1,45)) # 1~45이하


'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다. 
'''
from random import*
date = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월 "+str(date) +"일로 선정되었습니다.")
