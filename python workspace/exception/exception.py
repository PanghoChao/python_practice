#예외처리
try: #try 안에 있는 문장은 실행하는데 오류가 발생하면

    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    #nums.append( int(nums[0]/nums[1])) #리스트 안에 값이 없을때 list index out
    print("{0}/{1} ={2}".format(nums[0], nums[1],nums[2]))

except ValueError : #벨류 에러에 해당하면 아래를 실행합니다.
    print("에러! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err:
    print(err) # 에러문 출력

except Exception as err: #나머지 모든 에러
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)


#######################에러 발생시키기########################

try:  
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("첫번째 숫자를 입력하세요 : "))

    if num1>= 10 or num2 >= 10 :
        raise ValueError #에러문장으로 넘기고 이후 코드는 실행이 안댐
    print("{0}/{1} ={2}".format(num1, num2, int(num1/num2)))

except ValueError :
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력 하세요.")


########################사용자 정의 예외처리########################

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg= msg

    def __str__(self):
        return self.msg
try:  
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("첫번째 숫자를 입력하세요 : "))

    if num1>= 10 or num2 >= 10 :
        raise BigNumberError("입력값 : {0},{1}".format(num1, num2)) #에러문장으로 넘기고 이후 코드는 실행이 안댐
    print("{0}/{1} ={2}".format(num1, num2, int(num1/num2)))

except ValueError :
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력 하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력 하세요.")
    print(err)



######################## finally ########################

finally : 
    print("계산기를 이용해 주셔서 감사합니다.") #정상적이든, 에러이든 무조건 실행
