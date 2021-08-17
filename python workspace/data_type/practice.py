
# 파이썬은 프린트안에 숫자자료형 값을 넣을수 있다.
print(5)
print(-10)
print(3.14)


# 주석 설정 :  ctrl + /

#앞뒤로 작은 따옴표 3개씩 넣으면 주석처리됩니다.
'''
이렇게 하면
여러문장이 주석처리가 됩니다. 
'''


#문자열 프린트

print('풍선')
print("나비"*2)
# 참 /거짓 ---boolean

print(5>10) #false
print(5<10) #true
print(not True) #false
print(not False) #true

# 변수 
# 애완동물을 소개해주세요~
name = "해피"
animal = "고양이"
age = 4
hobby = "낮잠"
is_adult = age >= 3


print("우리집 강아지의 이름은 연탄이예요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요?True")
#아래처럼 치환가능

print("우리집 " + animal+"의 이름은 " + name + "예요")
print(name + "는 "+ str(age) + "살이며, "+ hobby +"을 아주 좋아해요")
print(name +"는 어른일까요?"+ str(is_adult))
#정수형을 문자열로 전환, 불린형을 문자열로 전환
# '+' 대신에 ',' 를 사용할 수있고, ','의 경우는 정수형, 문자열 구분안해도 되며 띄어쓰기가 들어간다.

'''

'''

station = "사당"

print(station+"행 열차가 들어오고 있습니다.")

station = "신도림"

print(station+"행 열차가 들어오고 있습니다.")

station = "인천공항"

print(station+"행 열차가 들어오고 있습니다.")


