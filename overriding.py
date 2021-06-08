class Car:
    def __init__(self, name = "car", brand = "HYUNDAI", color = "빨강", speed = 0):
        self.name = name
        self.brand = brand
        self.color = color
        self.speed = speed     # 인스턴스 변수

    def printSpeed(self):   # 멤버함수는 self를 반드시 첫 번째 매개변수로 가짐
        print(self.speed)

    def printColor(self):
        print(self.color)

    def upSpeed(self, value):
        self.speed += value 
        print("부모클래스 속도 : %d" %self.speed)
    def downSpeed(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0

class Sedan(Car):
    seatNum = 0
    def getSeatNum(self):
        return self.seatNum
    
    def upSpeed(self, value):
        self.speed += value
        print("자식클래스 속도 : %d" %self.speed)
        if self.speed > 150:
            self.speed = 150     

sedan1 = Sedan()
car1 = Car()
car1.upSpeed(10)
sedan1.upSpeed(100)