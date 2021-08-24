
###################################모듈사용##############################
#모듈은 확장자가 .py입니다.
##같은 경로이거나, 같은 파이썬 라이브러리 폴더에 모여있어야 사용가능

'''
import theater_module 

theater_module.price(3) #3명으로 사용
theater_module.price_morning(4)
theater_module.price_solider(5)

#
import theater_module as mv #as 로 별명 붙이기

mv.price(3)
mv.price_morning(4)
mv.price_solider(5) #위와 동일


from theater_module import*

price(3)
price_morning(4)
price_solider(5)


from theater_module import price, price_morning

price(3)
price_morning(4)
#불러오지 않았기에 오류 
# price_solider(5)


from theater_module import price_solider as price

price(5) #군인 할인 가격으로 나옴


'''
################################패키지##############################
#모듈들을 모아놓은 집합

# import travel.thailand #마지막은 모듈, 패키지

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

#from 은 모듈, 패키지, 클래스 다 불러올 수 있다.
# from travel.thailand import ThailandPackage # 클래스
# from travel import vietnam #모듈파일


################################__all __##############################
'''
from random import* #random 모듈
from travel import* 
trip_to = thailand.ThailandPackage() #공개 , 비공개가 구분되어있지 않기때문에 볼 수 가 없음
trip_to.detail()

trip_to = vietnam.veitnamPackage() 
trip_to.detail()


################################ 패키지, 모듈위치 ##############################
from travel import* 

import inspect
import random
print(inspect.getfile(random))  #패키지 위치찾기
print(inspect.getfile(thailand))  #lib 안에 있는 패키지 경로를 먼저 쓰임

'''

################################ pip install ##############################
#pip로 패키지 설치하기
#이미 잘만들어진 패키지가 많음
#google 검색창에 pypi 검색
# pip install --upgrade [패키지명]   => 업그레이드
# pip uninstall [패키지명]  => 삭제


# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


################################ 내장함수 ##############################
# input : 사용자입력을 받는 함수 
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

#dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random #외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst =[1, 2, 3]
# print(dir(lst)) #리스트에서 쓸 수 있는 함수가 쭉나옴

# name = "Jim"
# print(dir(name)) #이름에 대해서 쓸 수 있는 함수가 쭉나옴
#Built-in Function 내장함수에 대해서 나와있음
################################ 외장함수 ##############################
#import를 해서 불러와야하는 것들

#google 검생창에  list of python modules 
# python Module index  에서 외장함수 목록들을 볼 수 있다.


#glob : 경로 내의 폴더 /파일 목록 조회 (윈도우dir)

# import glob
# print(glob.glob("*.py")) #확장자가 py 인 모든파일

#os : 운영체제에서 제공하는 기본 기능 
# import os 
# print(os.getcwd()) #현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder, "폴더를 생성하였습니다.")



# import time #시간 관련 함수

# print(time.localtime())
# print(time.strftime("%Y -%m -%d  %H:%M:%S"))

import datetime 
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today+td) #오늘 부터 100일 후