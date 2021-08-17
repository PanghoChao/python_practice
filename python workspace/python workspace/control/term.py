'''
weather = input("오늘날씨는 어때요?")

# if 조건 : 
#     실행 명령문

if weather == "비" or weather == "눈" :
    print("우산을 챙기세요")

elif weather == "미세먼지" :
    print("마스크를 챙기세요.")
else :
    print("준비물 필요 없어요.")


temp = int(input("기온은 어때요?"))

if 30 <= temp :
    print("너무 더워요. 나가지마세요.")

elif 10<= temp <30  :
    print("괜찮은 날씨에요.")
    
elif 10 > temp :
    print("외투 챙기세요")
    
else : 
    print("너무 추워요. 나가지 마세요.")

'''

#################### 반복문 #########################
# for문
''' 
# for 변수 in [리스트](혹은 튜플, 문자열등)


for waiting_no in [0,1,2,3,4] : 
    print("대기번호 : {0}".format(waiting_no))

#randrange()
for waiting_num in range(1,6) : 
    print("대기번호 : {0}".format(waiting_num))


starbucks = ["아이언맨", "토르", "아이엠그루트"]
for customer in starbucks : 
    print("{0}, 커피가 준비되었습니다.".format(customer))

'''
# while문 
'''

customer = "토르"
index = 5 
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer,index))
    index -= 1
    if index == 0 :
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
index = 1 
while True :
    print("{0}, 커피가 준비되었습니다. ".format(customer))
    index += 1
    print("{0}호출하였습니다.".format(index))
    if index == 10 :
        break


customer = "토르"
person = "Unknow"
while person != customer :
    print("{0}, 커피가 준비되었습니다. ".format(customer))
    person =input("성함이 어떻게 되시죠?")
'''
# continue , break
'''
absent = [2, 5] #결석
no_book = [7] #책을 깜빡했음
for student in range(1, 11) : # 1 ~ 10
        if student in absent: 
            continue
        elif student in no_book : 
            print("{0}교무실로와".format(student))
            break
        else : 
           print("{0}, 책을 읽어봐".format(student))


'''
# 한줄 for 문
# 출석 번호가 1,2,3,4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
'''

student = [1,2,3,4,5]
print(student)
student = [i +100 for i in student]
print(student)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am grrot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students1 = ["Iron man", "Thor", "I am grrot"]
students1 = [i.upper() for i in students1]
print(students1)'''


Quiz) 당신은 COcoa 서비스를 이용하는 택시 기사님입니다. 
50명의 승객과 매칭 기회가 있을 떄, 총 탑승 승객수를 구하는 프로그램을 작성하시오.

조건 1: 승객별 운행소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건 2: 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...

[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분