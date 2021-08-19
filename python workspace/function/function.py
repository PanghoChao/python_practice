
def open_account(): #함수의 정의
    print("새로운 계좌가 개설되었습니다.")



open_account() #함수의 호출

########################### 전달값 과 반환값 ########################################
def deposit(balance, money): #입금 함수
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance + money




def withdraw(balance, money): #출금
    if balance >= money :  #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance-money
    else : 
        print("잔액이 부족합니다.잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money) : #저녁에 출금 
    commission = 100 # 수수료 100원
    return commission, balance - money - commission  #리턴값에 2개이상이면 튜플로 반환이 된다.



balance = 0 #잔액
balance = deposit(balance, 1000)
print(balance)
# balance = withdraw(balance, 500)
print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))


########################### 기본값 ########################################

def profile(name, age , main_lang):
    print("이름 : {0}\t나이 : {1}\t주사용언어 :{2}"
        .format(name, age, main_lang))

profile("유재석",20 , "파이썬")
profile("김태호",25 , "자바")


# 같은 학교 같은 학년 같은 반 같은 수업.
# 반복되는 값을 기본 값으로 대체 가능!

def profile(name, age = 17 , main_lang= "파이썬"): #기본으로 값을 받겠다는 의미
    print("이름 : {0}\t나이 : {1}\t주사용언어 :{2}"
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")

########################### 키워드값 ########################################


def profile(name, age , main_lang):
    print(name, age, main_lang)

profile(name ="유재석", main_lang="파이썬", age=20)
profile( main_lang="자바", age=25, name ="김태호")


########################### 가변인자 ########################################

# def profile(name, age , lang1, lang2, lang3, lang4, lang5 ):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = "") # end 는 안끝났다는 말
#     print(lang1, lang2, lang3, lang4, lang5)


# profile("유재석", 20 , "python", "java", "C", "C++", "C#")
# profile("김태호", 25 , "Kotlin", "Swift", "", "", "") # 매번 빈값을 넣어주기 힘듬

def profile(name, age , *language ):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = "") # end 는 안끝났다는 말
    for lang in language:
        print(lang, end = "")
    print()


profile("유재석", 20 , "python ", "java ", "C ", "C++ "  , "C#")
profile("김태호", 25 , "Kotlin ", "Swift")



########################### 지역변수 전역변수 ########################################

gun= 10 

def checkpoint(soldiers): #경계근무
    global gun #전역 변수 선언
    gun = gun -soldiers   #gun이 초기화 되지 않았다. #함수내에 변수는 밖의 함수와 무관
    print("[함수 내] 남은총 : {0}".format(gun))

def checkpoint_return(gun, soldiers): #경계근무
    gun = gun -soldiers
    print("[함수 내] 남은총 : {0}".format(gun))
    return gun    

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_return(gun, 2)
print("남은 총 : {0}".format(gun))



