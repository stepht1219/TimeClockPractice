#Lower2.py
#Stephanie Tattrie
#Create Date: 11/4/15

CONSTANT_FILE_LOCATION = "/home/h701887048/lab7_Stephanie_Tattrie/data/"


def f_writeFile():
    outfile = open(CONSTANT_FILE_LOCATION + "myoutfile.txt", 'w')
    while True:
        sentence = input("Enter a sentence or 99 to end: ")
        if sentence == "99":
            break
        else:
            outfile.write(sentence+" ")
    outfile.close()

def f_readFile():
    f = open(CONSTANT_FILE_LOCATION+"myoutfile.txt")
    string = ""
    line = ""
    for line in f:
        string = string + str(line)
    return string
    f.close()

def f_readLower():
    f = open(CONSTANT_FILE_LOCATION+"lower.txt")
    string = ""
    line = ""
    for line in f:
        string = str(line)
        print(string)
   # return f
    f.close()

def main():
    f_writeFile()
    s = f_readFile()
    string = ""
    for x in s:
        number = ord(x)
        if number in range(65,97):
            num1 = chr(number + 32)
        elif number in range(97,122):
            num1 = chr(number)
        else:
            num1 = " "
        string = string + num1
    #print(string)
    file = open(CONSTANT_FILE_LOCATION + "lower.txt", 'w')
    file.write(string)
    file.close()
    f_readLower()
main()
