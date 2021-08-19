
# 스타크래프트
'''
# 마린 : 공격 유닛 , 군인. 총을 쓸수 있음
name = "마린" #유닛이름
hp = 40
damage = 5

print("{}유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# 탱크 : 공격유닛, 탱크
tank_name = "탱크" #유닛이름
tank_hp = 150
tank_damage = 35

print("{}유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

tank2_name = "탱크" #유닛이름
tank2_hp = 150
tank2_damage = 35

print("{}유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp,tank2_damage))


def attack(name, location, damage) :
    print("{0} : {1}방향으로 적군을 공격 합니다. [공격력 {2}]". format(name,location,damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)
'''
#탱크가 많아지면, 수없이 반복하게된다. 

# #일반유닛
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{}유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))

# marine1 = Unit("마린", 40 , 5) #class로 만들어지는 놈들은 객체!
# marine2 = Unit("마린", 40 , 5)
# tank = Unit("탱크", 150 , 35)
# #marine3 = Unit("마린")

# ############################### init ###################################
# # 생성자
# # 클래스의 인스턴스 라고도 함. 
# # 클래스를 호출할 때 "init"이 정의 된 갯수 만큼 값을 받아야만 객체를 생성해줌

# ############################### 멤버변수 ###################################
# # 공중유닛, 비행기, 클로킹

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking =True


# if wraith2.clocking == True :
#     print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))
# ############################### 메소드 ###################################

# #공격유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
    
#     def attack(self, location):
#         print("{0} :{1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
#         .format(self.name , location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name , damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)


############################### 상속 ###################################
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp


# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
    
    # def attack(self, location):
    #     print("{0} :{1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
    #     .format(self.name , location, self.damage))

    # def damaged(self, damage):
    #     print("{0} : {1} 데미지를 입었습니다.".format(self.name , damage))
    #     self.hp -= damage
    #     print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    #     if self.hp <= 0:
    #         print("{0} : 파괴되었습니다.".format(self.name))

# # firebat1 = AttackUnit("파이어뱃", 50, 16)
# # firebat1.attack("5시")
# # firebat1.damaged(25)
# # firebat1.damaged(25)



# ########다중상속 
# #드랍쉽

# class Flyable :
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# #어택유닛과, 프라이어블 상속
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)


# 발키리 
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


########################## 메소드 오버라이딩 #############################
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):   # move 정의
        print("[지상 유닛 이동]")
        print("{0} :{1} 방향으로 이동합니다.[속도 {2}]"\
        .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed ,damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} :{1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
        .format(self.name , location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name , damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

#어택유닛과, 프라이어블 상속
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):   #move() 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


vulture = AttackUnit("벌쳐", 80, 10 ,20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시")


########################## pass #############################
#건물

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# #
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass


# game_start()
# game_over()

########################## super #############################
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name , hp, 0)
        super().__init__(name, hp, 0) #바로 위에 문장과 동일
        self.location = location