#!/usr/bin/python
# -*- coding: UTF-8 -*-
def LetterChanges(str): 
    newStr = ""
    for char in str:
      if char.isalpha():
          if char.lower() == 'z':
             char = 'a'
          else:
            char = chr( ord(char) + 1 )
      
      if char in "aeiou":
        char = char.upper()
      newStr = newStr + char
    
    return newStr


print( LetterChanges( input("please input letters\n") ) )