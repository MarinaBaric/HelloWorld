

#Tuples are immutable
#Packing
#Unpacking


#Strings are immutable
#join
#split
#Partition
y = "My name is {0} and I am {1} years old."
x = y.format("Marina", 26)
print(x)


#Range
#Lists start at 0
#range(stop), range(start, stop), range(start, stop, step) 


#enumerate
#Gives positions and corresponding value in list


#Lists
#Begin from end by running r[-1]
for i in range(len(r)):
    print(r[i])
    
    
#s[:2] ger de första två elementen. 0 fram till 2.
#Copy list by doing: r = listan.copy() or r = list(listan)
#listan.indec('fox') looks for the index of the word fox in the list
#del removes elements in list: del listan[3] removes the third elementen
#remove removes wanted element in list: listan.remove('fox')
#Check if value is in list or not by doing: 'fox' in listan or 'fox' not in listan
#Insert things in list by using listan.insert(index, value)
#You add elements to a list by extending, +, appending
#You change all elements by looping through list 
new list = [x+1 for x in my_list]
#Reverse or sort list by listan.reverse() and listan.sort()


#Dictionaries
y = {'Marre' : '1994'}
#keys with value
#We can update dictionaries with another dictionary
#Find key or values by printing keys or values
#From pprint import pprint as pp 
#pp(m) then provides a much easier way to read in alfabetic order for keys


#Sets
#Sets are often use to remove duplicates from random lists
#Set is immutable but elements must be immutable

