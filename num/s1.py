class Car:
    def __init__(self, m, c, s):
        self.__model = m
        self.__color__ = c
        self.__speed__ = s
    def getMode1(self):
        return self.__model
    def setModel(self, m):
        self.__model = m

    def speedUp(self): self.__speed__ +=10
    def speedDown(self): self.__speed__ -=10
    def __str__(self):
        return "Car[model=%s: color=%s, speed=%d]" % (self.__model, self.__color__, self.__speed__)
    
c = Car('BMW', 'balck', '100')
c.color = 'red'
c.setModel('Benz')
print(c)

    