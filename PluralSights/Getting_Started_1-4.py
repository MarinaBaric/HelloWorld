#import this

'''
for i in range(5):
    x = i*10
    print(x)
'''

'''
import math
print(math.sqrt(81))
'''

'''
while c!= 0:
    print(c)
    c -= 1

while c != 10:
    print(c)
    c += 1
    
while True:
    response = input()
    if int(response) % 7 == 0:
        break
'''

'''
#String
c = "stockholm"
c.capitalize()
a = 'hej'
b = 'hej'
c = a + ' ' + b
print(c)
'''

'''
#Bytes
svensk = "Jag körde över en bro och medan jag åkte så käkade jag en macka"
print(svensk)
data = svensk.encode('utf8')
print(data)
swedish = data.decode('utf8')
print(swedish)
if svensk == swedish:
    print('yes')
''' 

'''
#Lists
a = [1,9,8]
b = ['apple', 'orange', 'pear']
b[1] = a[1]
print(b)

c = []
c.append(2.43)
print(c)

d = [1,2,3]
for i in d:
    c.append(i)

print(c)

d.remove(2)
print(d)
'''

'''
#Dictionary
byear = {'marre' : '1994', 'feri' : '1992', 'bettan' : '1993'}

byear['fippe'] = '1994'
print(byear)
byear['fippe'] = '2000'
print(byear)
byear['fippe'] = '1994'
print(byear)
byear.pop('marre')
print(byear)

#for i in byear:
#    if i == 'bettan':
#        byear.pop(i)
#        print(byear)
        
for person in byear:
    print(person, byear[person]) #gives us the key and the value

'''

'''
#using a text from url as a text
from urllib.request import urlopen
story = urlopen('https://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)

story.close()
print(story_words)
'''