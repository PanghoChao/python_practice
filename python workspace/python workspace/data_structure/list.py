#####################리스트 []####################

#지하철 칸별로 10명 20명 30명
'''
subway1 = 10
subway2 = 20
subway3 = 30

subway = {10, 20, 30}
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))


#다음 정류장에서 하하씨가 탐
subway.append("하하") #맨뒤에 추가
print(subway)

#정형돈씨를 유재석/ 조세호 사이에 탐

subway.insert(1, "정형돈")  #중간에 삽입
print(subway.pop()) #맨뒤에 한명을 뺌
print(subway)

#같은 이름인 사람이 몇 명 있는 지 확인
subway.append("유재석") 
print(subway.count("유재석"))



#정렬도 가능 
num_list = [5,2,4,3,1]
num_list.sort() #순서대로
print(num_list)
num_list.reverse() #순서 뒤집기
print(num_list)
#num_list.clear() #모두지우기
print(num_list)

#다양한 자료형 함께 사용 가능

mix_list= ["조세호", 20 , True]
print(mix_list)

#리스트 합치기
num_list.extend(mix_list)
print(num_list)
'''


'''
#####################사전####################
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100]) 

print(cabinet.get(5)) #없는값이여도 오류나지않고 진행
print(cabinet.get(5), "사용가능") # None 대신 다른 값 넣기

#print(cabinet[5]) #오류값이면 그 즉시 종료

3 in cabinet #True
5 in cabinet #False

#새 손님
print(cabinet)
cabinet[20] = "조세호"
cabinet[3] = "김종국"
print(cabinet)

# 간 손님
del cabinet[3]
print(cabinet)

#key들만 출력
print(cabinet.keys())
#vlaue들만 출력
print(cabinet.values())

#둘다 쌍으로 출력
print(cabinet.items())

# 영업종료
cabinet.clear()
'''
'''
####################튜플####################
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
#menu.add("생선까스") // 튜플을 추가하거나 삭제가 불가능

#name = "김종국"
#age = 20
#hobby = "코딩"
#print(name, age, hobby)

#튜플은 한번에 선언가능
(name, age, hobby) = ("김종국", 20, "hobby")
print(name, age, hobby)


#####################집합 (set)#################### 
#중복이 안되고, 순서가 없음 추가 및 제거도 가능

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석","김태호","양세형"}
python = set(["유재석", "박명수"])


#교집합(java와 python을 모두 할 수 있는 사람)

print(java & python)
print(java.intersection(python))

#합집합 (java 혹은 python을 할 수 있는 개발자)

print(java| python)
print(java.union(python))

# 차집합 (java는 할 줄 알지만 python은 모르는 개발자)
print(java-python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹었어요
java.remove("김태호")
print(java)

'''
'''
####################자료구조의 변경 ####################
#커피숍
menu= {"커피", "우유", "주스"} #세트(집합)형식 - 중괄호
print(menu, type(menu))

menu = list(menu)           #리스트형식 - 대괄호
print(menu, type(menu)) 


menu = tuple(menu)          #튜플형식 - 소괄호
print(menu, type(menu))  

menu = set(menu)          #다시 집합형식 - 중괄호
print(menu, type(menu))  
'''

Quiz) 당신의 학교에는 파이썬 코딩대회를 주최합니다. 
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다. 
댓글 작성자들 중에 추첨을 통해 1명은 치킨,  3명은 커피 쿠폰을 받게 됩니다. 
추첨 프로그램을 작성하시오. 

조건 1 : 편의상 댓글은 20명이 작성 하였고 아이디는 1~20이라고 가정 
##list 20 을 만들어 준다. 
조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
##추첨은 세트(집합)으로 만들어준다. - 치킨 1명, 커피 3명

조건 3 : random 모듈의 suffle과 samlpe 을 활용

(출력 예제)
--당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)

from random import*
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))

