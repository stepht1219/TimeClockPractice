#Vowels.py
#Author: Stephanie Tattrie
#Create Date: 9/27/15

def main():
    sumv = 0
    v = 'AEIOUaeiou'
    word = input("Enter a word: ")
    for l in word:
        if l in v:
            sumv = sumv + 1

    print ("Number of vowels =", sumv)

main()
