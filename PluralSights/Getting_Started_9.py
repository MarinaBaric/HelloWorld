import sys
import os

'''
path = "C:\GitHub"
Number_Of_Files = 0
for files in os.walk(path):
    for files in path:
        Number_Of_Files = Number_Of_Files + 1
print("Total files = ",Number_Of_Files)
'''

iterable = ['spring', 'summer', 'autumn', 'winter']
'''
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) #will produce fail "StopIteration"
'''
'''
#Generator functions
def year():
    yield 100
    yield 200
    yield 300
    
years = year()
print(next(years))
print(next(years))
print(next(years))
print(next(years)) #will produce fail "StopIteration"
'''

file = open("test.txt","r")
row_count = 0
for row in file:
    row_count += 1
    
print(f"Row count is {row_count}")