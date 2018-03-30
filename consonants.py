#Consonants
#Author: Stephanie Tattrie
#Create Date: 9/27/15

def main():
    sumc = 0
    c = 'ZzYyXxWwVvTtSsRrPpQqMmNnLlKkJjHhGgFfDdCcBb'
    word = input("Enter a word: ")
    for l in word:
        if l in c:
            sumc = sumc + 1

    print ("Number of consonants =", sumc)

main()

