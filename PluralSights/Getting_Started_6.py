import sys


#Arguments and returns, Objects and Types
'''
m = [9, 15, 25]

def modify(k):
#Returns modified list with same id. This is not a copy. It is the same list.
    k.append(39)
    print("k =", k)
    
modify(m) 
'''

'''
f = [4,5,6]
def replace(k):
# Returns g but is not a new variable. It is only set by the function. f has same id.
    g = [7,8,9]
    print("g =", g)
    
replace(f) 
'''

'''
f = [4,5,6]
def replace(k):
# Will repace content in f but it has the same id since it is the same reference with replaced values.
    g = [7,8,9]
    print("g =", g)
    
replace(f) 
'''

'''
def banner(message="Marina Baric", border="*"):
#Creating a banner with exchangable arguments. Set message and border in command prompt if wanting a different border.
    line = border * len(message)
    print(line)
    print(message)
    print(line)
    
banner()
'''

'''
import time
def show(arg=time.ctime()):
#Function will not get new value in REPL. But will get new value in command prompt.    
    print(arg)
    
show()

def showoff():
#Function will get new value in REPL and command prompt. 
    print(time.ctime())

showoff()
'''

'''
count = 0
def show_count():
    print(count)
    
def set_count(c):
# Cannot change the count value since it is outside of the function
    count = c

def set_count(c):
    global count   #Sets the global value for the entire module
    count = c
'''
    
    
 