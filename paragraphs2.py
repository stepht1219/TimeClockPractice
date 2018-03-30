#paragraphs2.py
#Stephanie Tattrie
#Create Date 11/4/15


CONSTANT_FILE_LOCATION = "/home/h701887048/lab7_Stephanie_Tattrie/data/"

def f_readFile():
    f = open(CONSTANT_FILE_LOCATION+"paragraphs.txt")
    string = ""
    line = ""
    for line in f:
        string = str(line)
        string += string
    return(string)
    f.close()


def main():
    paragraph = f_readFile()
    #paragraph = input("Please enter a paragrpah, ending each sentence with a period: ")
    space = " "
    sentence = "."
    sumWords = 1
    sumSentences = 0
    for x in paragraph:
        if x in space:
            sumWords = sumWords + 1
    for x in paragraph:
        if x in sentence:
            sumSentences = sumSentences + 1
    print("The number of words in your paragrpah = ", sumWords)
    print("The number of sentences in your paragraph = ", sumSentences)


main()
