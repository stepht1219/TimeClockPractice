# lower.py                                                                     
# Stephanie Tattrie                                                            
# Create Date: 10/4/15                                                          

def main():
    string = ""
    word = input("Enter a word or a sentence: ")
    for r in word:
        wordnum = ord(r)
        if wordnum in range(97,122):
            num = (chr(wordnum))
        elif wordnum in range (65,90):
            num = (chr(wordnum + 32))
        else:
            num = " "
        string = string + num
    print(string)
main()

