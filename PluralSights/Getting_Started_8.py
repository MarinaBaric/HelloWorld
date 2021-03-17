import sys
import os

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
'''
# Convert a string to an integer from values set in dictionary above
def convert(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x = {x}")
    except (KeyError, TypeError):
        print("Conversion failed!")
    return x
'''
'''
def convert(s):
    #x = -1 removed to simplify even more
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        #x = int(number)
        return int(number) #instead of defining x and then printing it at the end
    except (KeyError, TypeError):
        #No print here creates an IndentationError so instead you can write:
        #pass #no-op
        return -1
    #return x
'''
'''
def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number) #instead of defining x and then printing it at the end
    except (KeyError, TypeError, ValueError) as e:
        print(f"Conversion error: {e!r}", file=sys.stderr)
        #return -1
        raise
         
from math import log

def string_log(s):
    v = convert(s)
    return log(v)
'''
'''
def sqrt(x):
    if x < 0:
        raise ValueError(
        "Cannot compute square root of " f"negative number {x}")
    #Compute square roots using the method of Heron of Alexandria
    #Returns the square root of x
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess
    
def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e: #ValueError (if input is of correct type but does not work and 
                            #Instead of ZeroDivisionError:
        print(e, file=sys.stderr)
    
    
    print("Program execution continues normally here.")
    
p = '/path/to/datafile.dat'
try:
    process_file(f)
except OSError as e:
    print(f'Error: {e}')
    
if __name__ == '__main__':
    main()
'''
'''
#check keypad imput 
try:
    import msvcrt
    def getkey():
    #Waits for keystring and returns single character strings
        return mscvrt.getch()
    
except:
    import sys
    import tty
    import termios
    def getkey():
    #Waits for keypress and return a single character string
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch
        
   #If either of the Unix-specific tty or termios are not found, 
   # we allow the ImportError to propagate from here
'''

import msvcrt
while True:
    pressedKey = msvcrt.getch()
    if pressedKey == 'q':    
       print("Q was pressed")
    elif pressedKey == 'x':    
       sys.exit()
    else:
       print("Key Pressed:" + str(pressedKey))
       
       
       