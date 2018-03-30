#compoundwords.py
#Author: Stephanie Tattrie




CONSTANT_FILE_LOCATION = "/Users/stephanietattrie/lab8_Stephanie_Tattrie/words"
import random
def f_readFile():
    f = open(CONSTANT_FILE_LOCATION+"compoundWords.txt")
    string = ""
    line = ""
    clist = []
    for line in f:
        string = str(line)
        clist.append(string)
    return clist
    f.close()

def main():
    print (f_readFile)
main()
