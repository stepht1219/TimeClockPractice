#Paragraphs.py                                                                 
#Author: Stephanie Tattrie                                                     
#Create Date:9/28/15                                                            

def main():
    sentence = input("Enter a paragraph: ")
    space = " "
    sumwords = 1
    period = "."
    sumsentence = 0
    for l in sentence:
        if l in space:
            sumwords = sumwords + 1
    for l in sentence:
        if l in period:
            sumsentence = sumsentence + 1
    print("The Number of Sentences = ",sumsentence)    
    print("The Number of Words  = ", sumwords)
main()
