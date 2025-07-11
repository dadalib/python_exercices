class FireSignal:
    # private attribute
    __height=12.0 # static attribut
    def __init__(self,colorInit=None,positionInit=None):
        # Can not surcharge python method
        # We can give values to attribute
        # self to avoid declare argument
        self.__color=colorInit or 0
        self.__position = positionInit or 0.0

    @staticmethod # Declare static method
    def setHeight(newHeight):
        FireSignal.__height = newHeight
    def changeColor(self,newColor):
        self.__color = newColor
        print("The color of the fire is : "+str(self.__color))
    @staticmethod
    def getHeight():
        print("The height of the fire is %s"%FireSignal.__height)
        # Not surcharge attribute values
    def blink(self,a=None,b=None):
        if a == None and b== None:
            print("First blink")
            for i in range(2):
                print("I am off")
            for j in range(2):
                print("I am on")

        elif a!=None  and b==None:
            print("Secon Blink")
            for i in range(2):
                for j in range(a):
                    print("I am off")
                for j in range(a):
                    print ("I am on")
        
        else:
            print("Third way")
            for i in range(2):
                for j in range(a):
                    print("I am off")
                for j in range(b):
                    print("I am on")
 # Constructor Call
oneFire = FireSignal(1,3)
# Constructor Surcharge
anotherFire = FireSignal(1)
oneFire.changeColor(3)
oneFire.setHeight(8.9)
FireSignal.getHeight()
anotherFire.setHeight(10.6)
oneFire.getHeight()
print("***Blink***")
oneFire.blink()
oneFire.blink(3)
b=oneFire.blink(2,3)








