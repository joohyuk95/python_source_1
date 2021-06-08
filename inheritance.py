class Car:
    count = 0       # 클래스 변수 ? 인스턴스 변수?

    def __init__(self, name = "car", brand = "HYUNDAI", color = "빨강", speed = 0):
        self.name = name
        self.brand = brand
        self.color = color
        self.speed = speed     # 인스턴스 변수
        Car.count += 1          # 클래스 변수

    def printSpeed(self):   # 멤버함수는 self를 반드시 첫 번째 매개변수로 가짐
        print(self.speed)

    def printColor(self):
        print(self.color)

    def upSpeed(self, value):
        self.speed += value 

    def downSpeed(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0

class Sedan(Car):
    seatNum = 0
    def getSeatNum(self):
        return self.seatNum

class Truck(Car):
    capacity = 0
    def getCapacity(self):
        return self.capacity

Sedan1 = Sedan()

Sedan1.upSpeed(100)
Sedan1.printSpeed()

Truck1 = Truck()
ca = Truck1.getCapacity()
print(ca)