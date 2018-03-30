#File example, open reading, writing files
#Created by Stephanie Tattrie
#Date Nov 4th

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

def f_readUpper():
    f = open(CONSTANT_FILE_LOCATION+"upper.txt")
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
        if number in range(65, 90):
            num1 = chr(number)
        elif number in range(97,122):
            num1 = chr(number - 32)
        else:
            num1 = " "
        string = string + num1
    file = open(CONSTANT_FILE_LOCATION + "upper.txt", 'w')
    file.write(string)
    file.close()
    f_readUpper()
main()
