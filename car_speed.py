class Car:
    __speed =0
    @staticmethod
    def speed_up(speedUP):
        Car.__speed+=speedUP
        print("Speed %s"%Car.__speed)
    def speed_down(self,speedDown):
        Car.__speed-=speedDown
        print("Speed %s"%Car.__speed)

MyCar=Car()
MyCar.speed_up(45)
MyCar.speed_down(15)

    