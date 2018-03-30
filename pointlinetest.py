#pointlinetest.py
#Stephanie Tattrie
#Create Date: 12/8/15

from pointlineclass import Point, Line

def makePoints():
    point1 = Point()
    x1 = float(input("Enter an X value: "))
    y1 = float(input("Enter a Y value: "))
    point1.setX(x1)
    point1.setY(y1)
    
    x2 = float(input("Enter an X value: "))
    y2 = float(input("Enter a Y value: "))
    
#    t = point1.getDistance(x1,y1)
#    print("\nDistance to point1 ", t)

#    n = point1.IsNear(10,29)
#    print("Is Near ", n)

    t = point1.getDistance(x2,y2)
    print("\nDistance to point1: %.2f "% t)

    n = point1.IsNear(x2,y2)
    print("Is Near ", n)

    point2 = Point()
    point2.setX(x2)
    point2.setY(y2)

    return point1,point2

def makeLine(p1, p2):
    l = Line()
    l.setPointA(p1)
    l.setPointB(p2)

    leng = l.calcLength()
    print("Length: %.2f"% leng)

    print("\nThe Line is made up of Point A and Point B ")
    print("Point A = ", l.getPointA())
    print("Point B = ", l.getPointB())

    n = l.calcSlope()
    print("Slope = ", n)
def main():
    p1, p2 = makePoints()
    makeLine(p1, p2)
main()
           
