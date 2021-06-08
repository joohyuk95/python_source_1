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

    def changeColor(self, color):
        self.color = color

    def getName(self):
        return self.name
    
    def getSpeed(self):
        return self.speed

    def getColor(self):
        return self.color

    def getMember(self, member):
        if member == "name":
            return self.getName()
        elif member == "speed":
            return self.getSpeed()
        elif member == "color":
            return self.getColor()
        else:
            return None

    def __del__(self):
        Car.count -= 1

# myCar1 = Car()       # 인스턴스 생성
# myCar2 = Car()
# myCar2.printColor()
# myCar2.printSpeed()
# myCar1.printColor()
# myCar1.printSpeed()
# myCar1.upSpeed(100)
# myCar1.printSpeed()

# myCar1.downSpeed(250)
# myCar1.printSpeed()

# myCar1.changeColor("blue")
# myCar1.printColor()

# print(myCar1.getName())
# print(myCar1.getMember("name"))

myCar1 = Car()
myCar1.speed = 30
print("자동차1의 현재 속도는 : %dkm, 생산된 자동차 숫자는 총 %d대입니다."
         %(myCar1.speed, Car.count))

myCar2 = Car()
myCar2.speed = 100
print("자동차2의 현재 속도는 : %dkm, 생산된 자동차 숫자는 총 %d대입니다."
         %(myCar2.speed, Car.count))

myCar3 = Car()
myCar3 = myCar1
myCar3.speed = 50
print("자동차3의 현재 속도는 : %dkm, 생산된 자동차 숫자는 총 %d대입니다."
         %(myCar1.speed, Car.count))

print(hex(id(myCar1.speed)))
print(hex(id(myCar3.speed)))

del myCar1
del myCar2
print(Car.count)