
# 문자열
# sentence = '나는 소년입니다'

# print(sentence)
# sentence2 = "파이썬은 쉬어요"
# print(sentence2)

# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬어요
# """
# print(sentence3)


#문자열 
'''
jumin = "990120-1234567"

print("성별 : "+ jumin[7]) #[]는 해당하는 위치의 문자를 가져올 수 있다.
print("연 : "+ jumin[0:2]) #0 부터 2 직전까지 =>( 0 ~ 1) 
print("월 : "+ jumin[2:4])  
print("일 : "+ jumin[4:6])
print("생년월일 : "+ jumin[:6]) #0은 생략가능  
print("뒤 7자리 : "+ jumin[7:]) #끝수도 생략가능     
print("뒤 7자리(뒤에서부터) : "+ jumin[-7:-1]) #맨뒷자리는 -1       
'''
'''
#문자열처리함수
python = "Python is Amazing"
print(python.lower()) # 소문자 전환
print(python.upper()) # 대문자 전환
print(python[0].isupper()) #맨 앞글자가 대문자인지 확인
print(len(python))
print(python.replace("Python", "Java"))


index = python.index("n") #첫번째 "n" 찾기
print(index)
index = python.index("n", index + 1) #두번째 "n" 찾기
print(index)

print(python.find("java")) # 값이 없으면 -1 반환
#print(python.index("java")) # 오류를 냄

print(python.count("n"))
'''

'''
#문자열 포맷
#방법1
print( "나는 %d살 입니다."% 20)
print( "나는 %s을 좋아해요."% "파이썬")
print("Apple 은 %c로 시작해요."% "A")

# %s 
print( "나는 %s살 입니다."% 20)
print( "나는 %s색과 %s색을 좋아해요."% ("파란","빨강"))



#방법2
print( "나는 {}살 입니다.".format(20))
print( "나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨강"))
print( "나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨강"))


#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

#방법4 (v3.6이상~)

age =20 
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
'''


'''
#탈출문자
print("백문이 불여일견\n백견이 불여일타")

print("저는 '팡호차오'입니다.")

'''
'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com

규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 =>naver
규칙3 : 남은 글자 중 처음 세사리 + 글자 갯수 + 글자내 "e"갯수 + "!"로구성

예) 생성된 비밀번호 : nav51!
'''

url = "http://naver.com"

pw = url.replace("http://" ,"")
pw = pw[:url.index(".")]
len = (len(pw))
e = (pw.count("e"))
pw2 = pw[:3]
print(f"{pw2}{len}{e}!")
