import os
import sys


NumList = [1721,299,55,77,99,675,1456,366,44,675,44,3333,22,97966,55,445]

#a = input("Enter elements: ").split()
#for i in range(len(a)):
#    a[i] = int(a[i])
#print(a)
'''
NumList = open('elements.txt').read().splitlines()
for i in range(len(NumList)):
    NumList[i] = int(NumList[i])
#print(NumList)
'''


def control_sum(mylist):
    x=0
    y=x+1
    new_list = [i+mylist[x] for i in mylist]
    new_new_list = [i+mylist[y] for i in new_list]
    if 2020 in new_list:
        print(mylist[x],"+",mylist[new_list.index(2020)],"=",mylist[x]+mylist[new_list.index(2020)])
        print(mylist[x],"*",mylist[new_list.index(2020)],"=",mylist[x]*mylist[new_list.index(2020)])
    else:
        x = x+1
        print("bajs")
        control_sum(mylist[x:])
    return control_sum

control_sum(NumList)





'''
sum of of three entries in list python
https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-9.php
https://www.geeksforgeeks.org/python-three-element-sum-in-list/
'''






