# Compute the average test scores for 4 tests
# Author: Stephanie Tattrie
# Create Date: 9/9/2015

CONSTANT_NUMBER = 4

def getScore():
    n = []
    for x in range (CONSTANT_NUMBER):
        i = int(input ("Enter the Score: "))
        n. append(i)
    return n

def sumNumbers(inScores):
    x = 0
    s = 0
    while x < CONSTANT_NUMBER:
        s = s + inScores[x]
        x = x + 1
    return s

def calcAvg(s, c):
    a = s / c
    return a


def main():
    #get Student Name
    studentName = input("Enter Student Name")
    
    # Get the Student Scor
    scores = getScore()

    # Sum up the Score
    sumScore = sumNumbers(scores)

    # Calc the Avg
    scoreAvg = calcAvg(sumScore, CONSTANT_NUMBER)

    print("Student Name :", studentName)
    print("Student Avg :", scoreAvg)

main()
