#!/usr/bin/python3
import re
def LongestWord(sen): 
    wordlist = re.findall(r"\w+",sen)
    myword = ""
    for word in wordlist:
        if len(word) > len(myword) :
            myword = word
    return myword
    
# keep this function call here  
print(LongestWord(input("please input words\n")))  