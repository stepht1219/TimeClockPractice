#Words.py
#Author: Stephanie Tattrie
#Create Date:9/28/15

def main():
    sentence = input("Enter a sentence: ")
    space = " "
    sumwords = 1
    for l in sentence:
        if l in space:
            sumwords = sumwords + 1
    print("The Number of Words  = ", sumwords)
main()
