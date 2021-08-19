class Unit :
    def __init__(self):
        print("유닛 생성자")

class Flyable:
    def __init__(self):
        print("Fly유닛 생성자")


class FlyableUint(Unit, Flyable):
    def __init__(self):
        super().__init__() #슈퍼는 다중상속에는 어울리지않음

#드랍쉽
dropship = FlyableUint()