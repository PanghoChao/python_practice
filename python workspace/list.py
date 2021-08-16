#리스트 []

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

#다양ㅎ산 자료형 함께 사용 가능

mix_list= ["조세호", 20 , True]
print(mix_list)

#리스트 합치기
num_list.extend(mix_list)
print(num_list)
'''



#사전
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