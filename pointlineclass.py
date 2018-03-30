#pointlineclass.py
#Stephanie Tattrie
#Create Date: 12/8/15

import math 

class Point:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x  = x
        return self.__x

    def getY(self):
        return self.__y

    def setY(self,y):
        self.__y  = y
        return self.__y

    def getDistance(self, x, y):
        x1 = self.getY()
        y1 = self.getX()
        diffx = abs(x1 - x)
        diffy = abs(y1 - y)
        distance = math.sqrt((diffx * diffx) + (diffy * diffy))
        return distance

    def IsNear(self, x, y):
        n = self.getDistance(x, y)
        if n <= 5:
            return "True"
        else:
            return "False"


    def __str__(self):
        return str(self.__x) + ',' +  str(self.__y)


class Line(Point):
    def __init__(self):
        Point.__init__(self)
        self.__A = Point()
        self.__B = Point()
        self.__slope = 0
        self.__length = 0

    def getPointA(self):
        return self.__A

    def getPointB(self):
        return self.__B

    def setPointA(self, p):
        self.__A.setX(p.getX())
        self.__A.setY(p.getY())
        return self.__A
    
    def setPointB(self, p):
        self.__B.setX(p.getX())
        self.__B.setY(p.getY())
        return self.__B

    def calcSlope(self):
        x1 = self.__A.getX()
        x2 = self.__B.getX()
        y1 = self.__A.getY()
        y2 = self.__B.getY()
        if x1 == x2:
            return "Slope is Undefined"
        else:
            self.__slope = (y2 - y1) / (x2 - x1)
            return self.__slope 
    


    def calcLength(self):
        x1 = self.__A.getX()
        x2 = self.__B.getX()
        y1 = self.__A.getY()
        y2 = self.__B.getY()
        diffx = abs(x2 - x1)
        diffy =abs(y2 - y1)
        distance = math.sqrt((diffx * diffx) + (diffy *diffy))
        return distance
