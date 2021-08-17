from random import*

users = range(1,21)  # 1~20
users = list(users)
# print(users)
shuffle(users)
print(users) 

winners = sample(users,4)

print("--당첨자 발표 --")
print("치킨당첨자 : {0}" .format(winners[0]))
print("커피당첨자 : {0}" .format(winners[1:]))
print("-- 축하합니다 --")
