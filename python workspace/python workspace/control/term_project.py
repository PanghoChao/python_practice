
from random import sample


operating_t = range(5,51) # 5분 ~50분
time = range(5,16)
count = 0
for i in range(1,51)  :# 50명의 승객

    t = sample(operating_t, 1)

    if  15 < t[0] < 51 : 
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(i, t[0]))

    else  :
        print("[O] {0}번째 손님 (소요시간 : {1})".format(i, t[0]))
        count += 1

print("총 탑승 승객 : {0}".format(count))    
    