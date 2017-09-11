#!/usr/bin/python3
def FirstFactorial(num) :
    if num == 1 :
      return 1
    else :
      return num*FirstFactorial( num-1 )
inputNum =  int( input("please input num\n") ) 
print(FirstFactorial( inputNum ) )