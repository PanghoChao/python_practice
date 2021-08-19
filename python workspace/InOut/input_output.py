#############################표준 입출력 ################################

print("Python" + "Java")
print("Python" ,"Java" ,sep=",") #빈공간을 지정해줄수있는 sep
print("Python" ,"Java" ,sep=",", end ='?') #원래는 end가 줄바꿈이지만, end = ? 으로 선언해줌
print("무엇이 더 재밌을까요?") 


import sys # 모듈
print("Python" ,"Java", file=sys.stdout) #표준 출력으로 문장이 찍힘
print("Python" ,"Java", file=sys.stderr) #표준 에러로 문장이 찍힘


scores = {"수학":0, "영어":50, "코딩": 100}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep = ":")  #ljust() 왼쪽정렬   #rjust() 오른쪽정력 #()안 숫자는 공간확보


#은행 대기 순번표
#001, 002, 003, ...
for num in range(1,21) :
    print("대기번호 : " + str(num).zfill(3)) #zfill 말그대로 '0'을 채우는


#표준 입력
answer = input("아무값이나 입력하세요  : ")
print(type(answer)) # 항상 문자열 형태로 값을 받는다.
print("입력하신 값은 "+ answer +"입니다.")



#############################다양한 출력포맷 ################################
#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) #{0:_>10}  _: 빈공간, > 오른쪽 정렬 , 10: 빈자리 수

# 양수일땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))  # +가 찍히도록 표기 
print("{0: >+10}".format(-500))  # 음수는 원래 -가 붙음

#왼쪽 정렬하고, 빈칸으로 _로 채움 
print("{0:_<+10}".format(500))

# 3자리 마다 ,(콤마) 를 찍어주기
print("{0:,}".format(100000000000))

# 3자리 마다 ,(콤마) 를 찍어주기, 부호도 붙이기
print("{0:+,}".format(100000000000))

# 3자리 마다 ,(콤마) 를 찍어주기, 부호도 붙이기, 자릿수 확보, 빈공간은 ^ 
print("{0:^<+30,}".format(100000000000))

#소수점 출력 
print("{0:f}".format(5/3))

#소수점 특정 자리수 까지만 표시 
print("{0:.2f}".format(5/3)) #(소수점 3째자리에서 반올림이 됨)

############################# 파일입출력 ################################
#쓰기
score_file = open("score.txt", "w", encoding="utf8") 
print("수학  : 0", file=score_file)
print("영어  : 50", file=score_file)
score_file.close() #항상 파일은 열었으면 닫아줘야댐

#이어쓰기
score_file = open("score.txt", "a", encoding="utf8") 
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") #줄바꿈 별도 필요
score_file.close() 

#읽기
score_file = open("score.txt", "r", encoding="utf8") 
print(score_file.read())
score_file.close()

#한줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8") 
print(score_file.readline()) #줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
print(score_file.readline(), end="")
print(score_file.readline())
print(score_file.readline())
score_file.close()


#몇줄인지 모를때 읽기
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line : 
      break
    print(line)

score_file.close()



#마지막 방법 읽기
score_file = open("score.txt", "r", encoding="utf8")
lines =score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()



############################# Pickle ################################
#프로그램을 파일형태로 저장하고 가져와서 프로그램으로 쓸수 있는 기능
import pickle
# pickle 쓰기
profile_file = open("profile.pickle", "wb")
profile = {"이름" : "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

# pickle 읽기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) 
print(profile)
profile_file.close()

############################# with ################################
import pickle
#with 오픈 with [명령어] as [변수]
with open("profile.pickle", "rb") as profile_file:  
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

 


